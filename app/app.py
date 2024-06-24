import logging
import asyncio
import requests
import concurrent.futures

from database.session import get_db_session
from database.initdb import init_db
from database import helpers as db
from database import models

from config import settings


def make_request(request: models.QueueRequest, timeout: int):
    try:
        response = requests.request(
            method=request.method, 
            url=f"{settings.BASE_URL}{request.uri}",
            params=request.params, 
            headers=request.headers, 
            timeout=timeout
        )
        return response
    except requests.exceptions.Timeout:
        logging.error(f"Request on {request.uri} timed out")
        return None


async def process_requests(reqs: list[models.QueueRequest]):
    with concurrent.futures.ThreadPoolExecutor(max_workers=settings.MAX_THREADS) as executor:
        future_to_request = {
            executor.submit(make_request, request, settings.TIMEOUT): request 
            for request in reqs
        }
        for future in concurrent.futures.as_completed(future_to_request):
            url = future_to_request[future]
            try:
                response = future.result()
                
                if not response:
                    logging.error(f"Request on {url.uri} failed")
                    continue

                logging.info(f"Request on {url.uri} succeeded")
                async with get_db_session() as session:
                    await db.save_response(
                        response=models.BaseQueueResponse(
                            status_code=response.status_code,
                            body=response.text,
                            req_id=url.req_id
                        ),
                        session=session
                    )
                    await db.mark_request_as_processed(request_id=url.req_id, session=session)
            except Exception as exc:
                logging.error(f"Request on {url.uri} generated an exception: {exc}")


async def run_service():
    reqs = await db.get_unprocessed_requests()
    if reqs:
        logging.info(f"Got {len(reqs)} requests to process")
        return await process_requests(reqs=reqs)
    logging.info("No unprocessed requests")


async def main():
    logging.getLogger("s1")
    await init_db()
    await run_service()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())


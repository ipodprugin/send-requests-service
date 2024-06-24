from typing import Optional
from . import dbmodels
from . import models
from .session import get_db_session

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert, select, update


async def get_unprocessed_requests():
    async with get_db_session() as session:
        requests = await session.execute(
            select(
                dbmodels.QueueRequests
            ).where(
                dbmodels.QueueRequests.processed == False
            )
        )
        requests = requests.scalars().all()
        if requests:
            return [models.QueueRequest.model_validate(request) for request in requests]


async def save_response(response: models.BaseQueueResponse, session: Optional[AsyncSession] = None):
    sql = insert(dbmodels.QueueResponses).values(
        status_code=response.status_code,
        body=response.body,
        req_id=response.req_id
    )
    if session:
        await session.execute(sql)
    else:
        async with get_db_session() as session:
            await session.execute(sql)


async def mark_request_as_processed(request_id: int, session: Optional[AsyncSession] = None):
    sql = update(dbmodels.QueueRequests).where(
        dbmodels.QueueRequests.req_id == request_id
    ).values(
        processed=True
    )
    if session:
        await session.execute(sql)
    else:
        async with get_db_session() as session:
            await session.execute(sql)


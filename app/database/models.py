from typing import Optional
from pydantic import BaseModel


class Base(BaseModel):
    class Config:
        from_attributes=True


class QueueRequest(Base):
    req_id: int
    uri: Optional[str]
    method: str
    params: Optional[dict]
    headers: Optional[dict]
    processed: bool


class BaseQueueResponse(Base):
    status_code: int
    body: Optional[str]
    req_id: int


class DBQueueResponse(BaseQueueResponse):
    resp_id: int


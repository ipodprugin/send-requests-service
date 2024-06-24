from sqlalchemy import (
    orm,
    Integer,
    String,
    Text,
    ForeignKey,
    Boolean,
    JSON,
)


class Base(orm.DeclarativeBase):
    pass


class QueueRequests(Base):

    __tablename__ = "queue_requests"

    req_id: orm.Mapped[int] = orm.mapped_column(Integer, primary_key=True)
    uri: orm.Mapped[str] = orm.mapped_column(String, nullable=True)
    method: orm.Mapped[str] = orm.mapped_column(String, nullable=False) 
    params: orm.Mapped[dict] = orm.mapped_column(JSON, nullable=True)
    headers: orm.Mapped[dict] = orm.mapped_column(JSON, nullable=True)
    processed: orm.Mapped[bool] = orm.mapped_column(Boolean, nullable=False, default=False)


class QueueResponses(Base):

    __tablename__ = "queue_responses"

    resp_id: orm.Mapped[int] = orm.mapped_column(Integer, primary_key=True)
    status_code: orm.Mapped[int] = orm.mapped_column(Integer, nullable=False)
    body: orm.Mapped[str] = orm.mapped_column(Text, nullable=True)
    req_id: orm.Mapped[int] = orm.mapped_column(
        ForeignKey(
            "queue_requests.req_id",
            ondelete="CASCADE"
        )
    )


from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from config import settings


engine = create_async_engine(settings.DB_URL.get_secret_value())
factory = async_sessionmaker(engine)


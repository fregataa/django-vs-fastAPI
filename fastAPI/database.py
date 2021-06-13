from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base

import models

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
SQLALCHEMY_DATABASE_URL = "postgresql+asyncpg://shlee:password@127.0.0.1:5432/todo"

Base = declarative_base()

engine = create_async_engine(
    # The argument below is needed only for SQLite,
    # since SQLite will only allow one thread to communicate with it.
    # https://fastapi.tiangolo.com/tutorial/sql-databases/#note
    SQLALCHEMY_DATABASE_URL,
    echo=True,
)

# expire_on_commit=False will prevent attributes from being expired
# after commit.
# create AsyncSession with expire_on_commit=False
AsyncSessionLocal = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


async def init_db():
    async with engine.begin() as conn:

        # Initailize db by dropping and creating all models
        await conn.run_sync(models.Base.metadata.drop_all)
        await conn.run_sync(models.Base.metadata.create_all)

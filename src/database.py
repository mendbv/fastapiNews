"""
Module for database connection
"""

<<<<<<< HEAD
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
=======
from typing import AsyncGenerator, Any

from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession
>>>>>>> master
from sqlalchemy.orm import DeclarativeBase

from .environs import *

DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_async_engine(url=DATABASE_URL)
<<<<<<< HEAD
session = async_sessionmaker(bind=engine, expire_on_commit=True)
=======
async_session = async_sessionmaker(bind=engine, expire_on_commit=True)
>>>>>>> master

class Base(DeclarativeBase):
    """
    Meta class for sqlalchemy ORM models
    """

<<<<<<< HEAD
=======
async def get_db() -> AsyncGenerator[Any, AsyncSession]:
    """
    Courutine for generating db session
    """
    async with async_session() as session:
        yield session
>>>>>>> master

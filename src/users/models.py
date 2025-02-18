"""
<<<<<<< HEAD
fastapi users
"""
from datetime import datetime
from typing import AsyncGenerator

from fastapi import Depends
from fastapi_users.db import SQLAlchemyBaseUserTableUUID, SQLAlchemyUserDatabase
from fastapi_users_db_sqlalchemy.access_token import (
    SQLAlchemyAccessTokenDatabase, 
    SQLAlchemyBaseAccessTokenTableUUID
)
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Mapped, mapped_column

from src.database import session as async_session, Base

class User(SQLAlchemyBaseAccessTokenTableUUID, Base):
    """
    user model
=======
User model
"""

from fastapi import Depends
from fastapi_users.db import SQLAlchemyBaseUserTableUUID, SQLAlchemyUserDatabase
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import Base, get_db


class User(SQLAlchemyBaseUserTableUUID, Base):
    """
    User model with UUID id column
>>>>>>> master
    """

    __tablename__ = "user"

<<<<<<< HEAD
    full_name: Mapped[str] = mapped_column(nullable=False)

class AccessToken(SQLAlchemyBaseAccessTokenTableUUID, Base):  
    pass


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session

async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)

async def get_access_token_db(
    session: AsyncSession = Depends(get_async_session),
):  
    yield SQLAlchemyAccessTokenDatabase(session, AccessToken)
=======
    full_name: Mapped[str] = mapped_column(String(length=100), nullable=False)
    comments: Mapped[list["Comment"]] = relationship("Comment", back_populates="news")


async def get_user_db(session: AsyncSession = Depends(get_db)):
    yield SQLAlchemyUserDatabase(session, User)


>>>>>>> master

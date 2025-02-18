"""
SQLalchemy ORM models
"""
<<<<<<< HEAD
from datetime import datetime

=======

from uuid import UUID
from datetime import datetime
>>>>>>> master

from sqlalchemy import ForeignKey, String, ARRAY
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base
<<<<<<< HEAD
=======
from src.users.models import User
>>>>>>> master

class Category(Base):
    """
    Category model
    """
    __tablename__ = "category"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(length=100), nullable=False)
    created: Mapped[datetime] = mapped_column(default=datetime.utcnow())

    news: Mapped[list["News"]] = relationship("News", back_populates="category")

class News(Base):
    """
    News model
    """
    __tablename__ = "news"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(length=100), nullable=False)
    content: Mapped[str | None] = mapped_column(nullable=True)
    images: Mapped[list[str | None]] = mapped_column(ARRAY(String), nullable=True)
    created: Mapped[datetime] = mapped_column(default=datetime.utcnow())
    updated: Mapped[datetime] = mapped_column(default=datetime.utcnow())

    category_id: Mapped[int | None] = mapped_column(
        ForeignKey("category.id", ondelete="SET NULL"), nullable=True
    )

    category: Mapped[Category | None] = relationship("Category", back_populates="news")
<<<<<<< HEAD


    # sudo docker run --name fast_db -e POSTGRES_PASSWORD=123456 -p 5432:5432 -d postgres
=======
    comments: Mapped[list["Comment"]] = relationship("Comment", back_populates="news")


    # sudo docker run --name fast_db -e POSTGRES_PASSWORD=123456 -p 5432:5432 -d postgres
    # alembic revision --autogenerate -m "comments"

class Comment(Base):
    """
    Comment model
    """
    __tablename__ = "comment"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    text: Mapped[str] = mapped_column(String(500), nullable=False)
    created: Mapped[datetime] = mapped_column(default=datetime.utcnow())
    updated: Mapped[datetime] = mapped_column(default=datetime.utcnow())

    news_id: Mapped[int] = mapped_column(
        ForeignKey("news.id", ondelete="CASCADE")
    )
    user_id: Mapped[UUID] = mapped_column(
        ForeignKey("user.id", ondelete="CASCADE")
    )

    news: Mapped[News] = relationship("News", back_populates="comments")
    user: Mapped[User] = relationship("User", back_populates="comments")


>>>>>>> master

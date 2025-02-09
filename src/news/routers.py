"""
Routers for news app
"""

from typing import Sequence

from fastapi import APIRouter, HTTPException
from sqlalchemy import select

from .models import Category, News
from .schemas import CategoryReadSchema, CategoryCreateSchema, NewsReadSchema, NewsCreateSchema

from src.database import session as async_session

category_router = APIRouter(
    prefix="/categories",
    tags=["Categories"]
)

news_router = APIRouter(
    prefix="/news",
    tags=["News"]
)

@category_router.get("", response_model=Sequence[CategoryReadSchema])
async def get_categories(offset: int = 0, limit: int = 10) -> Sequence[Category]:
    """
    Get all categories
    """
    async with async_session() as session:
        query = select(Category).offset(offset).limit(limit)
        result = await session.execute(query)
        categories = result.scalars().all()
        return categories


@category_router.get("/{category_id}", response_model=CategoryReadSchema)
async def get_category(category_id: int) -> Category:
    """
    Get category by id
    """
    async with async_session() as session:
        query = select(Category).filter(Category.id == category_id)
        result = await session.execute(query)
        category = result.scalar_one_or_none()
        if category is None:
            raise HTTPException(status_code=404, detail="Category not found")
        return category


@category_router.post("", response_model=CategoryReadSchema)
async def create_category(category: CategoryCreateSchema) -> Category:
    """
    Create category
    """
    async with async_session() as session:
        new_category = Category(**category.dict())
        session.add(new_category)
        await session.commit()
        await session.refresh(new_category)
        return new_category


@category_router.delete("/{category_id}")
async def delete_category(category_id: int) -> None:
    """
    Delete category by id
    """
    async with async_session() as session:
        query = select(Category).filter(Category.id == category_id)
        result = await session.execute(query)
        category = result.scalar_one_or_none()
        if category is None:
            raise HTTPException(status_code=404, detail="Category not found")
        await session.delete(category)
        await session.commit()


@category_router.put("/{category_id}", response_model=CategoryReadSchema)
async def update_category(category_id: int, category: CategoryCreateSchema) -> Category:
    """
    Update category by id
    """
    async with async_session() as session:
        query = select(Category).filter(Category.id == category_id)
        result = await session.execute(query)
        old_category = result.scalar_one_or_none()
        if old_category is None:
            raise HTTPException(status_code=404, detail="Category not found")

        for field, value in category.dict().items():
            setattr(old_category, field, value)

        await session.commit()
        await session.refresh(old_category)
        return old_category


@category_router.patch("/{category_id}", response_model=CategoryReadSchema)
async def partial_update_category(category_id: int, category: CategoryCreateSchema) -> Category:
    """
    Update category by id
    """
    async with async_session() as session:
        query = select(Category).filter(Category.id == category_id)
        result = await session.execute(query)
        old_category = result.scalar_one_or_none()
        if old_category is None:
            raise HTTPException(status_code=404, detail="Category not found")

        for field, value in category.dict().items():
            if value:
                setattr(old_category, field, value)

        await session.commit()
        await session.refresh(old_category)
        return old_category

# NEWS CRUD

@news_router.get("/{news_id}", response_model=NewsReadSchema)
async def get_news(news_id:int) -> News:
    """"
    Get all news
    """
    async with async_session() as session:
        query = select(News).filter(News.id == news_id)
        result = await session.execute(query)
        news = result.scalar_one_or_none()
        if news is None:
            raise HTTPException(status_code=404, detail="News not found")
        return news

@news_router.get("/{news_id}", response_model=Sequence[NewsReadSchema])
async def get_new_by_id(news_id: int) -> News:
    """
    Get news by id
    """
    async with async_session() as session:
        query = select(News).filter(News.id == news_id)
        result = await session.execute(query)
        news = result.scalar_one_or_none()
        if news is None:
            raise HTTPException(status_code=404, detail="News not found")
        return news
    
@news_router.post("", response_model=NewsReadSchema)
async def create_news(news: NewsCreateSchema) -> News:
    """
    Create news
    """
    async with async_session() as session:
        new_news = News(**news.dict())
        session.add(new_news)
        await session.commit()
        await session.refresh(new_news)
        return new_news
    
@news_router.delete("/{news_id}")
async def delete_news(news_id: int) -> None:
    """
    Delete news by id
    """
    async with async_session() as session:
        query = select(News).filter(News.id == news_id)
        result = await session.execute(query)
        news = result.scalar_one_or_none()
        if news is None:
            raise HTTPException(status_code=404, detail="News not found")
        await session.delete(news)
        await session.commit()

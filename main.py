"""
<<<<<<< HEAD
Main frogramm module
=======
Main program module
>>>>>>> master
"""

from fastapi import FastAPI

<<<<<<< HEAD
from src.news import category_router, news_router
from src.users import users_router

app = FastAPI()

app.include_router(router=category_router)
app.include_router(router=news_router)
app.include_router(router=users_router)
=======
from src.news import routers
from src.users import users_router
from src.media import media_router

app = FastAPI()

app.include_router(router=routers.categories_router)
app.include_router(router=routers.news_router)
app.include_router(router=users_router)
app.include_router(router=media_router)
>>>>>>> master

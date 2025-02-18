<<<<<<< HEAD
=======
"""
Users router
"""

>>>>>>> master
import uuid

from fastapi import APIRouter
from fastapi_users import FastAPIUsers

from .models import User
from .manager import get_user_manager
from .auth import auth_backend
<<<<<<< HEAD
from .schemas import *
=======
from .schemas import UserRead, UserCreate, UserUpdate
>>>>>>> master

fastapi_users = FastAPIUsers[User, uuid.UUID](
    get_user_manager,
    [auth_backend],
)

<<<<<<< HEAD
users_router = APIRouter(
    prefix="/api/users",
    tags=["Users"]
)

users_router.include_router(
    fastapi_users.get_auth_router(auth_backend)
)

users_router.include_router(
    fastapi_users.get_register_router(
        user_schema=UserRead,
        user_create_schema=UserCreate,
    ),
    prefix="/register",
    tags=["Register"]
)

users_router.include_router(
    fastapi_users.get_users_router(
        user_schema=UserRead,
        user_update_schema=UserUpdate
    ),
    prefix="",
    tags=["Users"]
)
=======
users_router = APIRouter()

users_router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

users_router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

users_router.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)
>>>>>>> master

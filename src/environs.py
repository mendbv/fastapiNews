"""
Module reads environ variables
"""

import os

from dotenv import load_dotenv

load_dotenv()

DB_NAME = os.getenv("DB_NAME", "postgres")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "password")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")

<<<<<<< HEAD
=======
JWT_SECRET = os.getenv("JWT_SECRET", "SECRET")
USER_MANAGER_SECRET = os.getenv("USER_MANAGER_SECRET", "SECRET")

MEDIA_ROOT = "media/"

>>>>>>> master
__all__ = [
    "DB_NAME",
    "DB_USER",
    "DB_PASSWORD",
    "DB_HOST",
    "DB_PORT",
<<<<<<< HEAD
=======
    "JWT_SECRET",
    "USER_MANAGER_SECRET",
    "MEDIA_ROOT",
>>>>>>> master
]

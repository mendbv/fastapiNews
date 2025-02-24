from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
import jwt
from ..models import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"

def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    user = verify_token(token)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    return user

def verify_token(token: str) -> User:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("sub")
        if user_id is None:
            return None
        user = get_user_by_id(user_id)  # Функция получения пользователя из базы данных
        return user
    except jwt.PyJWTError:
        return None

def get_user_by_id(user_id: int) -> User:
    # Пример функции для получения пользователя из базы данных или словаря
    # В реальном проекте вы будете использовать ORM (например, SQLAlchemy)
    users = [
        User(id=1, username="john_doe"),
        User(id=2, username="jane_doe"),
    ]
    return next((user for user in users if user.id == user_id), None)

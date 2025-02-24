from fastapi import APIRouter, HTTPException
from ..schemas import CommentCreate, CommentResponse
from typing import List
from .dependencies import get_current_user

from fastapi import Depends
from ..models import User


router = APIRouter(
    prefix="/comments", tags=["Comments"]
)

comments_db = []  # Имитация

@router.post("/", response_model=CommentResponse)
async def create_comment(comment: CommentCreate, current_user: User = Depends(get_current_user)):
    new_comment = {
        "id": len(comments_db) + 1,
        "text": comment.text,
        "author": current_user.username
    }
    comments_db.append(new_comment)
    return new_comment

@router.get("/", response_model=List[CommentResponse])
async def get_comments():
    return comments_db

@router.get("/{comment_id}", response_model=CommentResponse)
async def get_comment(comment_id: int):
    for comment in comments_db:
        if comment["id"] == comment_id:
            return comment
    raise HTTPException(status_code=404, detail="Comment not found")

@router.put("/{comment_id}", response_model=CommentResponse)
async def update_comment(comment_id: int, updated_comment: CommentCreate, current_user: User = Depends(get_current_user)):
    for comment in comments_db:
        if comment["id"] == comment_id:
            if comment["author"] != current_user.username:
                raise HTTPException(status_code=403, detail="You are not the owner of this comment")
            comment["text"] = updated_comment.text
            comment["author"] = current_user.username
            return comment
    raise HTTPException(status_code=404, detail="Comment not found")

@router.delete("/{comment_id}")
async def delete_comment(comment_id: int, current_user: User = Depends(get_current_user)):
    global comments_db
    for comment in comments_db:
        if comment["id"] == comment_id:
            if comment["author"] != current_user.username:  # Проверка, является ли пользователь владельцем
                raise HTTPException(status_code=403, detail="You are not the owner of this comment")
            comments_db = [comment for comment in comments_db if comment["id"] != comment_id]
            return {"detail": "Comment deleted"}
    raise HTTPException(status_code=404, detail="Comment not found")
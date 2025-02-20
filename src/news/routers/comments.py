from fastapi import APIRouter, HTTPException
from ..schemas import CommentCreate, CommentResponse
from typing import List

router = APIRouter(
    prefix="/comments", tags=["Comments"]
)

comments_db = []  # Имитация

@router.post("/", response_model=CommentResponse)
async def create_comment(comment: CommentCreate):
    new_comment = {
        "id": len(comments_db) + 1,
        "text": comment.text,
        "author": comment.author
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
async def update_comment(comment_id: int, updated_comment: CommentCreate):
    for comment in comments_db:
        if comment["id"] == comment_id:
            comment["text"] = updated_comment.text
            comment["author"] = updated_comment.author
            return comment
    raise HTTPException(status_code=404, detail="Comment not found")

@router.delete("/{comment_id}")
async def delete_comment(comment_id: int):
    global comments_db
    comments_db = [comment for comment in comments_db if comment["id"] != comment_id]
    return {"detail": "Comment deleted"}
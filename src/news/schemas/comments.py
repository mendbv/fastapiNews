"""
Comment schema
"""


import datetime

from pydantic import BaseModel
from uuid import UUID

from pydantic import BaseModel

class CommentReadSchema(BaseModel):

    id: int
    text: str
    created: datetime
    updated: datetime
    user_id: UUID

    class Config:
        arbitrary_types_allowed = True

class CommentCreate(BaseModel):
    text: str
    author: str

class CommentResponse(BaseModel):
    id: int
    text: str
    author: str
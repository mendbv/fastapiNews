"""
Comment schema
"""


import datetime

from pydantic import BaseModel
from uuid import UUID


class CommentReadSchema(BaseModel):

    id: int
    text: str
    created: datetime
    updated: datetime
    user_id: UUID

    class Config:
        arbitrary_types_allowed = True
# schemas/todo.py
from pydantic import BaseModel, Field
from typing import Optional

class TodoCreate(BaseModel):
    title: str = Field(..., min_length=1)
    description: Optional[str] = None

class TodoUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    completed: Optional[bool]

class TodoOut(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool
    user_id: int

    class Config:
        orm_mode = True

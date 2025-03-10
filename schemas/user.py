# schemas/user.py
from pydantic import BaseModel, EmailStr, Field
from typing import Optional
import enum

class RoleEnum(str, enum.Enum):
    user = "user"
    admin = "admin"

class UserCreate(BaseModel):
    usern: str = Field(..., min_length=3, max_length=30)
    email: EmailStr
    password: str = Field(..., min_length=6)
    role: Optional[RoleEnum] = RoleEnum.user

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr
    role: RoleEnum

    class Config:
        orm_mode = True

from typing import Optional
from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    id: int
    email: str
    username:str
    salary:str
    date:str
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False

    class Config:
        orm_mode = True


class UserCreate(schemas.BaseUserCreate):
    username: str
    salary: int
    date: str
    email: str
    password: str
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False
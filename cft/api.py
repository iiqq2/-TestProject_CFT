from typing import Union

from fastapi import Depends, FastAPI
from fastapi_users import fastapi_users, FastAPIUsers
from sqlalchemy.orm import Session

from auth.database import User
from auth.manager import get_user_manager
from auth.auth import auth_backend
from auth.schemas import UserCreate, UserRead

from core.db import *
from crud import *
from micro import models


app = FastAPI()

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)


app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

current_user = fastapi_users.current_user()
current_super_user = fastapi_users.current_user(superuser=True)

@app.get("/userdata")
def get_userdata(user: User = Depends(current_user), db: Session = Depends(get_db)):
    if user.is_superuser == True:
        return get_users(db)
    return f"Hello, вот ваша зарплата - {user.salary} и вот дата повыщения {user.date}"

@app.delete("/delete_user")
def delete_userdata(username: str,user: User = Depends(current_super_user), db: Session = Depends(get_db)):
    delete_user(name=username, db=db)
    return "Succes"

@app.put("/update_userdata")
def update_userdata(username: str, salary:Union[int, None] = None, date: Union[str, None] = None, user: User = Depends(current_super_user), db: Session = Depends(get_db)):
    update_user(name=username, salary=salary, date=date, db=db)
    return "Data was successfully updated"
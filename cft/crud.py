from sqlalchemy.orm import Session
from micro.models import Users


def get_users(db:Session):
    users = db.query(Users).all()
    return users

def delete_user(name, db:Session):
    user = db.query(Users).filter(Users.username==name).first()
    db.delete(user)
    db.commit()

def update_user(name, salary, date, db):
    if salary != None:
        db.query(Users).filter(Users.username==name).update({Users.salary:salary})
        db.commit()
    if date != None:
        db.query(Users).filter(Users.username==name).update({Users.date:date})
        db.commit()
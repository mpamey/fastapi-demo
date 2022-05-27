from fastapi import status, HTTPException, Depends, APIRouter
from typing import Any

from sqlalchemy.orm import Session
from app import models, database, schemas, utils, oauth2


router = APIRouter(
    prefix="/users",
    tags=['Users']
)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user(users: schemas.UserCreate,
                db: Session = Depends(database.get_db)
                ) -> Any:
    hashed_password = utils.hash(users.password)
    users.password = hashed_password

    new_user = models.Users(**users.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    db.close()
    return new_user


@router.get("/{user_id}", response_model=schemas.UserOut)
def get_user(user_id: int, db: Session = Depends(database.get_db)) -> Any:
    user = (db
            .query(models.Users)
            .filter(models.Users.user_id == user_id)
            .first()
            )

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id: {user_id} does not exist")
    return user

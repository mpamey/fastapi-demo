import datetime
from typing import Optional, Any
from pydantic import (BaseModel,
                      StrictStr,
                      StrictInt,
                      EmailStr,
                      )
from pydantic.types import conint


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    user_id: int
    email: EmailStr
    created_at: datetime.datetime

    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None


class PostBase(BaseModel):
    title: StrictStr
    content: str
    published: Optional[bool] = True
    rating: Optional[StrictInt] = None


class PostCreate(PostBase):
    pass


class PostResponse(PostBase):
    id: int
    created_at: datetime.datetime
    user_id: int
    user: UserOut

    class Config:
        orm_mode = True


class PostOut(BaseModel):
    Post: PostResponse
    votes: int



class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)

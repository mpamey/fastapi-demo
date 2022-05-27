from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP, text, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base


class Posts(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, nullable=False, server_default="True")
    rating = Column(Integer, nullable=True)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    user_id = Column(Integer, ForeignKey("users.user_id", ondelete="CASCADE"), nullable=False)

    user = relationship("Users")

class Users(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

class Vote(Base):
    __tablename__ = "votes"
    user_id = Column(Integer, ForeignKey("users.user_id", ondelete="CASCADE"), primary_key=True)
    post_id = Column(Integer, ForeignKey("posts.id", ondelete="CASCADE"), primary_key=True)

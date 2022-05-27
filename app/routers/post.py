from fastapi import Response, status, HTTPException, Depends, APIRouter
from typing import List, Any, Optional

from sqlalchemy import func
from sqlalchemy.orm import Session
from app import models, database, schemas, oauth2


router = APIRouter(
    prefix="/posts",
    tags=['Posts']
)


@router.get("/", response_model=List[schemas.PostResponse])
def get_posts(db: Session = Depends(database.get_db),
              current_user: int = Depends(oauth2.get_current_user),
              limit: int = 10,
              skip: int = 0,
              search: Optional[str] = "") -> Any:
    posts = db.query(models.Posts).filter(models.Posts.title.contains(search)).limit(limit).offset(skip).all()

    return posts


@router.delete("/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(post_id: int, db: Session = Depends(database.get_db),
                current_user: int = Depends(oauth2.get_current_user)) -> Any:

    deleted_post = (db.query(models.Posts)
                    .filter(models.Posts.id == post_id)
                    )
    if deleted_post.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with id: {post_id} was not found.")
    if deleted_post.first().user_id != current_user.user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Not authorized to perform requested action.")

    deleted_post.delete(synchronize_session=False)
    db.commit()
    db.close()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.get("/{post_id}", response_model=schemas.PostResponse)
def get_post(post_id: int,
             db: Session = Depends(database.get_db)
             ) -> Any:
    post = (db.query(models.Posts)
            .filter(models.Posts.id == post_id)
            .first()
            )
    db.close()
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with id: {post_id} was not found.")
    return post


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.PostResponse)
def create_post(posts: schemas.PostCreate,
                db: Session = Depends(database.get_db),
                current_user: int = Depends(oauth2.get_current_user)
                ) -> Any:
    new_post = models.Posts(user_id=current_user.user_id, **posts.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    db.close()
    return new_post

@router.put("/{post_id}", response_model=schemas.PostResponse)
def update_post(post_id: int,
                posts: schemas.PostCreate,
                db: Session = Depends(database.get_db),
                current_user: int = Depends(oauth2.get_current_user)
                ) -> Any:

    update_query = db.query(models.Posts).filter(models.Posts.id == post_id)

    updated_post = update_query.first()

    if updated_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with id: {post_id} was not found.")
    if updated_post.user_id != current_user.user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Not authorized to perform requested action.")
    update_query.update(posts.dict(),
                        synchronize_session=False)
    db.commit()
    updated_post = update_query.first()
    db.close()
    return updated_post

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from typing import List
from app.routers import post, user, auth, vote


app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def include_routers(app: FastAPI, routerlist: List) -> None:
    for router in routerlist:
        app.include_router(router)


include_routers(app, [post.router, user.router, auth.router, vote.router])

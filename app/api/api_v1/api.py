from fastapi import APIRouter

from app.api.api_v1.endpoints import auth, healthcheck, posts, users, votes

api_router = APIRouter()

api_router.include_router(healthcheck.router, tags=["status"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(posts.router, prefix="/posts", tags=["posts"])
api_router.include_router(votes.router, prefix="/votes", tags=["votes"])
api_router.include_router(auth.router, tags=["auth"])

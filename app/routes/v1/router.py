from fastapi import APIRouter

from app.routes.v1 import auth, user, candidates, votes, elections

api_router = APIRouter()
api_router.include_router(auth.router)
api_router.include_router(user.router)
api_router.include_router(candidates.router)
api_router.include_router(votes.router)
api_router.include_router(elections.router)

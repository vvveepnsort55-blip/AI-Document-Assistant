from fastapi import APIRouter

from api.documents import router as documents_router
from api.chat import router as chat_router
from api.auth import router as auth_router



router = APIRouter()



router.include_router(
    documents_router
)


router.include_router(
    chat_router
)


router.include_router(
    auth_router
)
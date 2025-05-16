from fastapi import APIRouter, Depends
from app.core.config import settings
from app.core.auth import get_current_user
from app.models.user import User

router = APIRouter(prefix=f"{settings.API_V1_STR}/datasources", tags=["datasources"])

@router.get("/")
def get_datasources(current_user: User = Depends(get_current_user)):
    """
    Get all datasources (placeholder).
    """
    return {"message": "Get datasources endpoint"}
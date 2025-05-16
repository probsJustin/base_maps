from fastapi import APIRouter, Depends
from app.core.config import settings
from app.core.auth import get_current_user
from app.models.user import User

router = APIRouter(prefix=f"{settings.API_V1_STR}/datamaps", tags=["datamaps"])

@router.get("/")
def get_datamaps(current_user: User = Depends(get_current_user)):
    """
    Get all datamaps (placeholder).
    """
    return {"message": "Get datamaps endpoint"}
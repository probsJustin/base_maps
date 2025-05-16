from fastapi import APIRouter, Depends
from app.core.config import settings
from app.core.auth import get_current_user
from app.models.user import User

router = APIRouter(prefix=f"{settings.API_V1_STR}/layers", tags=["layers"])

@router.get("/")
def get_layers(current_user: User = Depends(get_current_user)):
    """
    Get all layers (placeholder).
    """
    return {"message": "Get layers endpoint"}
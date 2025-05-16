from typing import Any, List, Optional

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.core.auth import get_current_user
from app.core.config import settings
from app.database import get_db
from app.models.user import User
from app.schemas.feature import Feature, FeatureCreate, FeatureUpdate, FeatureCollection
from app.services import feature_service

router = APIRouter(prefix=f"{settings.API_V1_STR}/features", tags=["features"])


@router.get("/", response_model=List[Feature])
def get_features(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: User = Depends(get_current_user),
) -> Any:
    """Get all features."""
    features = feature_service.get_features(db, skip=skip, limit=limit)
    return features


@router.post("/", response_model=Feature)
def create_feature(
    feature_in: FeatureCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> Any:
    """Create a new feature."""
    feature = feature_service.create_feature(db, feature_in, current_user)
    return feature


@router.get("/{feature_id}", response_model=Feature)
def get_feature(
    feature_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> Any:
    """Get a specific feature."""
    feature = feature_service.get_feature(db, feature_id)
    if not feature:
        raise HTTPException(status_code=404, detail="Feature not found")
    return feature


@router.put("/{feature_id}", response_model=Feature)
def update_feature(
    feature_id: int,
    feature_in: FeatureUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> Any:
    """Update a feature."""
    feature = feature_service.get_feature(db, feature_id)
    if not feature:
        raise HTTPException(status_code=404, detail="Feature not found")
    
    updated_feature = feature_service.update_feature(db, feature_id, feature_in, current_user)
    return updated_feature


@router.delete("/{feature_id}")
def delete_feature(
    feature_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> Any:
    """Delete a feature."""
    feature = feature_service.get_feature(db, feature_id)
    if not feature:
        raise HTTPException(status_code=404, detail="Feature not found")
    
    feature_service.delete_feature(db, feature_id)
    return {"status": "success", "message": "Feature deleted"}


@router.get("/{feature_id}/geojson", response_model=dict)
def get_feature_geojson(
    feature_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> Any:
    """Get a feature as GeoJSON."""
    feature = feature_service.get_feature_geojson(db, feature_id)
    if not feature:
        raise HTTPException(status_code=404, detail="Feature not found")
    return feature
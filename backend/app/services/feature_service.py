from typing import List, Optional, Dict, Any
from sqlalchemy.orm import Session
from geoalchemy2.shape import from_shape, to_shape
from geoalchemy2.functions import ST_AsGeoJSON
from shapely.geometry import shape
import json

from app.models.feature import Feature
from app.models.user import User
from app.schemas.feature import FeatureCreate, FeatureUpdate


def get_features(db: Session, skip: int = 0, limit: int = 100) -> List[Feature]:
    """Get all features with pagination."""
    return db.query(Feature).offset(skip).limit(limit).all()


def get_feature(db: Session, feature_id: int) -> Optional[Feature]:
    """Get a specific feature by ID."""
    return db.query(Feature).filter(Feature.id == feature_id).first()


def create_feature(db: Session, feature: FeatureCreate, current_user: User) -> Feature:
    """Create a new feature."""
    # Convert GeoJSON geometry to WKB for PostGIS
    geom_shape = shape(feature.geometry)
    wkb_geom = from_shape(geom_shape)
    
    db_feature = Feature(
        name=feature.name,
        description=feature.description,
        feature_type=feature.feature_type,
        geometry=wkb_geom,
        properties=feature.properties,
        created_by=current_user.id,
        updated_by=current_user.id
    )
    db.add(db_feature)
    db.commit()
    db.refresh(db_feature)
    return db_feature


def update_feature(
    db: Session, 
    feature_id: int, 
    feature_update: FeatureUpdate, 
    current_user: User
) -> Optional[Feature]:
    """Update an existing feature."""
    db_feature = get_feature(db, feature_id)
    if not db_feature:
        return None
    
    update_data = feature_update.dict(exclude_unset=True)
    
    # Handle geometry update if present
    if "geometry" in update_data:
        geom_shape = shape(update_data["geometry"])
        update_data["geometry"] = from_shape(geom_shape)
    
    # Update fields
    for field, value in update_data.items():
        setattr(db_feature, field, value)
    
    # Set updated_by
    db_feature.updated_by = current_user.id
    
    db.commit()
    db.refresh(db_feature)
    return db_feature


def delete_feature(db: Session, feature_id: int) -> bool:
    """Delete a feature."""
    db_feature = get_feature(db, feature_id)
    if not db_feature:
        return False
    
    db.delete(db_feature)
    db.commit()
    return True


def get_feature_geojson(db: Session, feature_id: int) -> Optional[Dict[str, Any]]:
    """Get a feature as GeoJSON."""
    result = db.query(
        Feature.id,
        Feature.name,
        Feature.description,
        Feature.feature_type,
        Feature.properties,
        ST_AsGeoJSON(Feature.geometry).label('geometry')
    ).filter(Feature.id == feature_id).first()
    
    if not result:
        return None
    
    # Create GeoJSON feature
    feature = {
        "type": "Feature",
        "id": result.id,
        "geometry": json.loads(result.geometry),
        "properties": {
            "name": result.name,
            "description": result.description,
            "feature_type": result.feature_type,
            **(result.properties or {})
        }
    }
    
    return feature
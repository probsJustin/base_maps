from typing import Optional, Dict, Any, List
from pydantic import BaseModel, Field
from datetime import datetime
from geojson_pydantic import Feature as GeoJSONFeature, FeatureCollection, Geometry


class FeatureBase(BaseModel):
    name: str
    description: Optional[str] = None
    feature_type: str  # point, line, polygon
    properties: Optional[Dict[str, Any]] = Field(default_factory=dict)


class FeatureCreate(FeatureBase):
    geometry: Dict[str, Any]  # GeoJSON geometry


class FeatureUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    feature_type: Optional[str] = None
    geometry: Optional[Dict[str, Any]] = None
    properties: Optional[Dict[str, Any]] = None


class FeatureInDBBase(FeatureBase):
    id: int
    created_by: Optional[int] = None
    updated_by: Optional[int] = None
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True


class Feature(FeatureInDBBase):
    geometry: Dict[str, Any]  # GeoJSON geometry


class FeatureCollection(BaseModel):
    type: str = "FeatureCollection"
    features: List[GeoJSONFeature]
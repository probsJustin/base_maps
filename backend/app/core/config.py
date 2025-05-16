from pydantic_settings import BaseSettings
from typing import List, Optional, Dict, Any
from pydantic import validator


class Settings(BaseSettings):
    PROJECT_NAME: str = "Base Maps API"
    PROJECT_DESCRIPTION: str = "A mapping project API with PostgreSQL and PostGIS"
    PROJECT_VERSION: str = "0.1.0"
    API_V1_STR: str = "/api"
    
    # CORS
    ALLOW_ORIGINS: List[str] = ["http://localhost:5173"]
    ALLOW_CREDENTIALS: bool = True
    ALLOW_METHODS: List[str] = ["*"]
    ALLOW_HEADERS: List[str] = ["*"]
    
    # Database
    DATABASE_URL: str = "postgresql://postgres:postgres@db/basemaps"
    
    # Security
    SECRET_KEY: str = "temporarysecretkeychangeforproduction"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # Environment
    ENVIRONMENT: str = "development"
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True


settings = Settings()
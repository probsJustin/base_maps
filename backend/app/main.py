from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from app.core.config import settings
from app.database import get_db
from app.core.init_db import init_db
from app.routes import (
    auth_router,
    user_router,
    role_router,
    feature_router,
    layer_router,
    datamap_router,
    datasource_router,
    network_router,
    application_router,
    picklist_router,
    notification_router,
    settings_router,
    usage_router,
)

# Create FastAPI app
app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.PROJECT_DESCRIPTION,
    version=settings.PROJECT_VERSION,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    docs_url=f"{settings.API_V1_STR}/docs",
    redoc_url=f"{settings.API_V1_STR}/redoc",
)

# Set up CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOW_ORIGINS,
    allow_credentials=settings.ALLOW_CREDENTIALS,
    allow_methods=settings.ALLOW_METHODS,
    allow_headers=settings.ALLOW_HEADERS,
)

# Include routers
app.include_router(auth_router)
app.include_router(user_router)
app.include_router(role_router)
app.include_router(feature_router)
app.include_router(layer_router)
app.include_router(datamap_router)
app.include_router(datasource_router)
app.include_router(network_router)
app.include_router(application_router)
app.include_router(picklist_router)
app.include_router(notification_router)
app.include_router(settings_router)
app.include_router(usage_router)


# Root endpoint
@app.get("/")
def root():
    return {
        "message": "Welcome to Base Maps API",
        "docs": f"{settings.API_V1_STR}/docs",
    }


# Startup event
@app.on_event("startup")
def startup_event():
    db = next(get_db())
    init_db(db)
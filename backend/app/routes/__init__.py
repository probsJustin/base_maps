# Import all router modules
from app.routes.auth_router import router as auth_router
from app.routes.user_router import router as user_router
from app.routes.role_router import router as role_router
from app.routes.feature_router import router as feature_router
from app.routes.layer_router import router as layer_router
from app.routes.datamap_router import router as datamap_router
from app.routes.datasource_router import router as datasource_router
from app.routes.network_router import router as network_router
from app.routes.application_router import router as application_router
from app.routes.picklist_router import router as picklist_router
from app.routes.notification_router import router as notification_router
from app.routes.settings_router import router as settings_router
from app.routes.usage_router import router as usage_router

# Export all routers
__all__ = [
    "auth_router",
    "user_router",
    "role_router",
    "feature_router",
    "layer_router",
    "datamap_router",
    "datasource_router",
    "network_router",
    "application_router",
    "picklist_router",
    "notification_router",
    "settings_router",
    "usage_router",
]
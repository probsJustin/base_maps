import logging
from sqlalchemy.orm import Session

from app.core.auth import get_password_hash
from app.models.user import User
from app.models.role import Role
from app.core.config import settings

logger = logging.getLogger(__name__)

# Initial user data
FIRST_SUPERUSER = "admin"
FIRST_SUPERUSER_PASSWORD = "admin"
FIRST_SUPERUSER_EMAIL = "admin@example.com"

def init_db(db: Session) -> None:
    """Initialize the database with initial data."""
    # Create default roles if they don't exist
    admin_role = db.query(Role).filter(Role.name == "admin").first()
    if not admin_role:
        admin_role = Role(name="admin", description="Administrator with all permissions")
        db.add(admin_role)
        logger.info("Created admin role")
    
    user_role = db.query(Role).filter(Role.name == "user").first()
    if not user_role:
        user_role = Role(name="user", description="Standard user")
        db.add(user_role)
        logger.info("Created user role")
    
    db.commit()
    
    # Create first superuser if it doesn't exist
    user = db.query(User).filter(User.email == FIRST_SUPERUSER_EMAIL).first()
    if not user:
        user = User(
            username=FIRST_SUPERUSER,
            email=FIRST_SUPERUSER_EMAIL,
            hashed_password=get_password_hash(FIRST_SUPERUSER_PASSWORD),
            is_active=True,
            is_superuser=True,
            role_id=admin_role.id
        )
        db.add(user)
        db.commit()
        logger.info("Created first superuser")
    else:
        logger.info("Superuser already exists")
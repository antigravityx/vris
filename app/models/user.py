"""
User model
"""
from sqlalchemy import Column, String, DateTime, JSON, Enum as SQLEnum
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
import uuid
import enum

from app.database import Base


class AppSource(str, enum.Enum):
    """Application sources"""
    LIBRO = "libro"
    VERIXMUSIC = "verixmusic"
    DASHBOARD = "dashboard"
    OTHER = "other"


class User(Base):
    """User model - centralized across all apps"""
    __tablename__ = "users"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    app_source = Column(SQLEnum(AppSource), nullable=False)
    external_id = Column(String(255), nullable=True)  # ID from source app
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    last_active = Column(DateTime, default=datetime.utcnow, nullable=False)
    metadata = Column(JSON, default=dict)  # Flexible metadata
    
    def __repr__(self):
        return f"<User {self.id} from {self.app_source}>"

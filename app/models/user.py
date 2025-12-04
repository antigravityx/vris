"""
User model
"""
from sqlalchemy import Column, String, DateTime, JSON, Enum as SQLEnum
from app.models.types import UUID
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
    
    id = Column(UUID(), primary_key=True, default=uuid.uuid4)
    app_source = Column(SQLEnum(AppSource), nullable=False, default=AppSource.OTHER)
    external_id = Column(String(255), nullable=True)  # ID from source app
    
    # Auth fields (Sovereign Identity)
    email = Column(String(255), unique=True, nullable=True, index=True)
    username = Column(String(50), unique=True, nullable=True, index=True)
    password_hash = Column(String(255), nullable=True)
    
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    last_active = Column(DateTime, default=datetime.utcnow, nullable=False)
    user_metadata = Column(JSON, default=dict)  # Flexible metadata
    
    def __repr__(self):
        return f"<User {self.id} ({self.email or 'no-email'})>"

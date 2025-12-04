"""
Event tracking model
"""
from sqlalchemy import Column, String, DateTime, JSON, BigInteger, ForeignKey, Integer
from app.models.types import UUID
from datetime import datetime

from app.database import Base


class UserEvent(Base):
    """User event tracking"""
    __tablename__ = "user_events"
    
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    user_id = Column(UUID(), ForeignKey("users.id"), nullable=False)
    event_type = Column(String(100), nullable=False)  # e.g., 'book_view', 'song_play'
    event_data = Column(JSON, default=dict)  # Flexible event data
    timestamp = Column(DateTime, default=datetime.utcnow, nullable=False)
    app_source = Column(String(50), nullable=False)
    
    def __repr__(self):
        return f"<UserEvent {self.event_type} by {self.user_id}>"


class UserPreference(Base):
    """Learned user preferences"""
    __tablename__ = "user_preferences"
    
    user_id = Column(UUID(), ForeignKey("users.id"), primary_key=True)
    preferences = Column(JSON, default=dict)  # e.g., {'genres': ['rock', 'jazz'], 'topics': ['tech']}
    confidence_score = Column(String(10), default="0.0")  # How confident we are
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f"<UserPreference for {self.user_id}>"

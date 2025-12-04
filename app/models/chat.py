"""
Chat and Message models for Soul Chat
"""
from sqlalchemy import Column, String, DateTime, Table, ForeignKey, Text
from app.models.types import UUID
from sqlalchemy.orm import relationship
from datetime import datetime
import uuid

from app.database import Base

# Association table for many-to-many relationship between Users and Chats
chat_participants = Table(
    'chat_participants',
    Base.metadata,
    Column('chat_id', UUID(), ForeignKey('chats.id'), primary_key=True),
    Column('user_id', UUID(), ForeignKey('users.id'), primary_key=True)
)

class Chat(Base):
    """Chat room model (P2P or Group)"""
    __tablename__ = "chats"
    
    id = Column(UUID(), primary_key=True, default=uuid.uuid4)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    
    # Relationships
    participants = relationship("User", secondary=chat_participants, backref="chats")
    messages = relationship("Message", back_populates="chat", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<Chat {self.id}>"

class Message(Base):
    """Message model"""
    __tablename__ = "messages"
    
    id = Column(UUID(), primary_key=True, default=uuid.uuid4)
    chat_id = Column(UUID(), ForeignKey('chats.id'), nullable=False)
    sender_id = Column(UUID(), ForeignKey('users.id'), nullable=False)
    content = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    
    # Relationships
    chat = relationship("Chat", back_populates="messages")
    sender = relationship("User")
    
    def __repr__(self):
        return f"<Message {self.id} from {self.sender_id}>"

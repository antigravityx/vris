"""
Prediction model
"""
from sqlalchemy import Column, String, DateTime, JSON, BigInteger, Float, ForeignKey
from app.models.types import UUID
from datetime import datetime

from app.database import Base


class Prediction(Base):
    """Store predictions made by ML models"""
    __tablename__ = "predictions"
    
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    user_id = Column(UUID(), ForeignKey("users.id"), nullable=False)
    prediction_type = Column(String(50), nullable=False)  # 'churn', 'purchase', 'recommendation'
    prediction_value = Column(JSON, default=dict)  # The actual prediction data
    confidence = Column(Float, default=0.0)  # Confidence score 0-1
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    
    def __repr__(self):
        return f"<Prediction {self.prediction_type} for {self.user_id}>"


class MLModel(Base):
    """Track ML models trained"""
    __tablename__ = "ml_models"
    
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    model_name = Column(String(100), nullable=False)
    model_type = Column(String(50), nullable=False)  # 'recommendation', 'classification', etc.
    version = Column(String(20), nullable=False)
    accuracy = Column(Float, default=0.0)
    trained_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    model_path = Column(String(255), nullable=True)  # Path to saved model
    model_metadata = Column(JSON, default=dict)  # Training params, etc.
    
    def __repr__(self):
        return f"<MLModel {self.model_name} v{self.version}>"

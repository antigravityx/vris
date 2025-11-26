"""
Configuration settings for VRIS
"""
from pydantic_settings import BaseSettings
from typing import List
import os


class Settings(BaseSettings):
    """Application settings"""
    
    # App
    APP_NAME: str = "VRIS"
    VERSION: str = "0.1.0"
    ENVIRONMENT: str = "development"
    DEBUG: bool = True
    
    # Database
    DATABASE_URL: str = "postgresql://vris:vris123@localhost:5432/vris_db"
    
    # Redis
    REDIS_URL: str = "redis://localhost:6379"
    CACHE_TTL: int = 300
    CACHE_ENABLED: bool = True
    
    # Security
    SECRET_KEY: str = "super-secret-key-change-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # API Keys
    API_KEY_LIBRO: str = "libro-api-key"
    API_KEY_VERIXMUSIC: str = "verixmusic-api-key"
    API_KEY_DASHBOARD: str = "dashboard-api-key"
    
    # Hugging Face
    HUGGINGFACE_API_KEY: str = ""
    
    # CORS
    CORS_ORIGINS: List[str] = [
        "http://localhost:3000",
        "http://localhost:5000",
        "http://localhost:8080",
        "https://libro.github.io"
    ]
    
    # ML Models
    ML_MODELS_PATH: str = "./app/ml/models/"
    RETRAIN_INTERVAL_HOURS: int = 24
    
    # Logging
    LOG_LEVEL: str = "INFO"
    
    class Config:
        env_file = ".env"
        case_sensitive = True


# Create settings instance
settings = Settings()

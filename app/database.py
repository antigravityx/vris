"""
Database configuration and session management
"""
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import declarative_base
from app.config import settings
import logging

logger = logging.getLogger(__name__)

# Convert PostgreSQL URL to async format if needed
if settings.DATABASE_URL.startswith("postgresql://"):
    database_url = settings.DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://")
else:
    database_url = settings.DATABASE_URL

# Configure engine args based on DB type
engine_args = {
    "echo": settings.DEBUG,
    "future": True,
}

if "sqlite" in database_url:
    engine_args["connect_args"] = {"check_same_thread": False}
else:
    engine_args["pool_pre_ping"] = True
    engine_args["pool_size"] = 5
    engine_args["max_overflow"] = 10

# Create async engine
engine = create_async_engine(
    database_url,
    **engine_args
)

# Create async session factory
AsyncSessionLocal = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# Base class for models
Base = declarative_base()


async def get_db():
    """Dependency to get database session"""
    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()


async def init_db():
    """Initialize database tables"""
    try:
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        logger.info("✅ Database initialized successfully")
    except Exception as e:
        logger.error(f"❌ Database initialization error: {e}")
        raise

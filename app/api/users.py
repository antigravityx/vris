"""
Users endpoints
"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from pydantic import BaseModel
from datetime import datetime
from typing import Optional, Dict, Any
import uuid

from app.database import get_db
from app.models.user import User, AppSource
from app.models.event import UserEvent, UserPreference
from app.api.auth import verify_api_key

router = APIRouter()


class UserTrackRequest(BaseModel):
    user_id: Optional[str] = None
    external_id: Optional[str] = None
    event_type: str
    event_data: Dict[str, Any] = {}


class UserInsightsResponse(BaseModel):
    user_id: str
    app_source: str
    total_events: int
    preferences: Dict[str, Any]
    last_active: datetime


@router.post("/track")
async def track_event(
    request: UserTrackRequest,
    app_source: str = Depends(verify_api_key),
    db: AsyncSession = Depends(get_db)
):
    """
    Track user event
    
    Creates or updates user and logs event for analytics
    """
    try:
        # Find or create user
        user = None
        if request.user_id:
            result = await db.execute(
                select(User).where(User.id == uuid.UUID(request.user_id))
            )
            user = result.scalar_one_or_none()
        elif request.external_id:
            result = await db.execute(
                select(User).where(
                    User.external_id == request.external_id,
                    User.app_source == AppSource(app_source)
                )
            )
            user = result.scalar_one_or_none()
        
        if not user:
            user = User(
                app_source=AppSource(app_source),
                external_id=request.external_id
            )
            db.add(user)
            await db.flush()
        
        # Update last active
        user.last_active = datetime.utcnow()
        
        # Create event
        event = UserEvent(
            user_id=user.id,
            event_type=request.event_type,
            event_data=request.event_data,
            app_source=app_source
        )
        db.add(event)
        
        await db.commit()
        
        return {
            "status": "success",
            "user_id": str(user.id),
            "event_tracked": True
        }
    
    except Exception as e:
        await db.rollback()
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{user_id}/insights", response_model=UserInsightsResponse)
async def get_user_insights(
    user_id: str,
    app_source: str = Depends(verify_api_key),
    db: AsyncSession = Depends(get_db)
):
    """Get user insights and analytics"""
    try:
        # Get user
        result = await db.execute(
            select(User).where(User.id == uuid.UUID(user_id))
        )
        user = result.scalar_one_or_none()
        
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        
        # Count events
        event_result = await db.execute(
            select(UserEvent).where(UserEvent.user_id == user.id)
        )
        events = event_result.scalars().all()
        
        # Get preferences
        pref_result = await db.execute(
            select(UserPreference).where(UserPreference.user_id == user.id)
        )
        preferences = pref_result.scalar_one_or_none()
        
        return UserInsightsResponse(
            user_id=str(user.id),
            app_source=user.app_source.value,
            total_events=len(events),
            preferences=preferences.preferences if preferences else {},
            last_active=user.last_active
        )
    
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/segments")
async def get_user_segments(
    app_source: str = Depends(verify_api_key),
    db: AsyncSession = Depends(get_db)
):
    """Get user segmentation (placeholder for ML clustering)"""
    return {
        "message": "User segmentation endpoint",
        "status": "coming_soon",
        "description": "Will use ML clustering to segment users"
    }

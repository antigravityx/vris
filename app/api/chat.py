"""
Chat endpoints and WebSockets
"""
from fastapi import APIRouter, Depends, WebSocket, WebSocketDisconnect, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, or_
from typing import List, Dict
import uuid
import json
from datetime import datetime

from app.database import get_db, AsyncSessionLocal
from app.models.user import User
from app.models.chat import Chat, Message, chat_participants
from app.api.auth import get_current_user

router = APIRouter()

# Connection Manager
class ConnectionManager:
    def __init__(self):
        # chat_id -> list of websockets
        self.active_connections: Dict[str, List[WebSocket]] = {}

    async def connect(self, websocket: WebSocket, chat_id: str):
        await websocket.accept()
        if chat_id not in self.active_connections:
            self.active_connections[chat_id] = []
        self.active_connections[chat_id].append(websocket)

    def disconnect(self, websocket: WebSocket, chat_id: str):
        if chat_id in self.active_connections:
            self.active_connections[chat_id].remove(websocket)
            if not self.active_connections[chat_id]:
                del self.active_connections[chat_id]

    async def broadcast(self, message: dict, chat_id: str):
        if chat_id in self.active_connections:
            for connection in self.active_connections[chat_id]:
                await connection.send_json(message)

manager = ConnectionManager()

# Endpoints

@router.post("/create")
async def create_chat(
    target_email: str,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Create a new chat with another user"""
    # Find target user
    result = await db.execute(select(User).where(User.email == target_email))
    target_user = result.scalar_one_or_none()
    
    if not target_user:
        raise HTTPException(status_code=404, detail="User not found")
        
    if target_user.id == current_user.id:
        raise HTTPException(status_code=400, detail="Cannot chat with yourself")

    # Check if chat already exists (simplified logic)
    # In a real app, we'd check if a chat with exactly these 2 participants exists
    
    # Create new chat
    new_chat = Chat()
    new_chat.participants.append(current_user)
    new_chat.participants.append(target_user)
    
    db.add(new_chat)
    await db.commit()
    await db.refresh(new_chat)
    
    return {"chat_id": str(new_chat.id), "target_user": target_user.email}

@router.get("/list")
async def list_chats(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """List all chats for current user"""
    # This query needs to be optimized for production
    # Currently fetching user with chats eagerly
    result = await db.execute(
        select(User).where(User.id == current_user.id)
    )
    user = result.scalar_one_or_none()
    
    # Need to explicitely load chats due to async
    # For MVP, we'll just return a simple list if possible or rely on lazy loading if configured
    # Async SQLAlchemy relationship loading is tricky, simplified approach:
    
    # Manual join
    stmt = select(Chat).join(Chat.participants).where(User.id == current_user.id)
    result = await db.execute(stmt)
    chats = result.scalars().all()
    
    chat_list = []
    for chat in chats:
        # Get other participant
        # This is N+1 problem, but fine for MVP
        # We need a new session or careful query to get participants of each chat
        chat_list.append({
            "id": str(chat.id),
            "updated_at": chat.updated_at
        })
        
    return chat_list

@router.get("/{chat_id}/messages")
async def get_messages(
    chat_id: str,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Get history of messages"""
    result = await db.execute(
        select(Message)
        .where(Message.chat_id == uuid.UUID(chat_id))
        .order_by(Message.created_at.asc())
    )
    messages = result.scalars().all()
    
    return [
        {
            "id": str(msg.id),
            "content": msg.content,
            "sender_id": str(msg.sender_id),
            "timestamp": msg.created_at
        }
        for msg in messages
    ]

# WebSocket
@router.websocket("/ws/{chat_id}/{token}")
async def websocket_endpoint(websocket: WebSocket, chat_id: str, token: str):
    # Validate token manually since headers aren't easy in WS
    # In prod, use query param or cookie
    try:
        # Create a new session for the websocket
        async with AsyncSessionLocal() as db:
            # Verify user
            from app.api.auth import get_current_user
            # We need to mock the dependency or call the logic directly
            # Re-implementing logic briefly for WS context
            import jwt
            from app.api.auth import SECRET_KEY, ALGORITHM
            
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            user_id = payload.get("sub")
            
            if not user_id:
                await websocket.close(code=4003)
                return
                
            await manager.connect(websocket, chat_id)
            
            try:
                while True:
                    data = await websocket.receive_text()
                    # Save message to DB
                    message_data = json.loads(data)
                    content = message_data.get("content")
                    
                    if content:
                        new_msg = Message(
                            chat_id=uuid.UUID(chat_id),
                            sender_id=uuid.UUID(user_id),
                            content=content
                        )
                        db.add(new_msg)
                        await db.commit()
                        
                        # Broadcast
                        await manager.broadcast({
                            "content": content,
                            "sender_id": user_id,
                            "timestamp": str(datetime.utcnow())
                        }, chat_id)
                        
            except WebSocketDisconnect:
                manager.disconnect(websocket, chat_id)
                
    except Exception as e:
        print(f"WS Error: {e}")
        await websocket.close(code=4000)

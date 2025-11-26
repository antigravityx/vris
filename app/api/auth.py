"""
Authentication endpoints
"""
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from datetime import datetime, timedelta
from jose import JWTError, jwt
from pydantic import BaseModel

from app.config import settings

router = APIRouter()
security = HTTPBearer()


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    app_source: str | None = None


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    """Create JWT access token"""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt


async def verify_api_key(credentials: HTTPAuthorizationCredentials = Depends(security)) -> str:
    """Verify API key from Authorization header"""
    api_key = credentials.credentials
    
    # Check against known API keys
    valid_keys = {
        settings.API_KEY_LIBRO: "libro",
        settings.API_KEY_VERIXMUSIC: "verixmusic",
        settings.API_KEY_DASHBOARD: "dashboard"
    }
    
    if api_key in valid_keys:
        return valid_keys[api_key]
    
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid API key"
    )


async def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)) -> TokenData:
    """Verify JWT token"""
    token = credentials.credentials
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        app_source: str = payload.get("sub")
        if app_source is None:
            raise credentials_exception
        token_data = TokenData(app_source=app_source)
    except JWTError:
        raise credentials_exception
    
    return token_data


@router.post("/token", response_model=Token)
async def login(app_source: str = Depends(verify_api_key)):
    """
    Get access token using API key
    
    Use your API key in Authorization header:
    ```
    Authorization: Bearer your-api-key-here
    ```
    """
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": app_source}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/verify")
async def verify(token_data: TokenData = Depends(verify_token)):
    """Verify current token"""
    return {
        "status": "valid",
        "app_source": token_data.app_source
    }

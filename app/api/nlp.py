"""
NLP (Natural Language Processing) endpoints
"""
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from typing import Optional

from app.api.auth import verify_api_key

router = APIRouter()


class SentimentRequest(BaseModel):
    text: str


class SentimentResponse(BaseModel):
    text: str
    sentiment: str  # 'positive', 'negative', 'neutral'
    score: float  # -1 to 1
    confidence: float


class SummarizeRequest(BaseModel):
    text: str
    max_length: Optional[int] = 150


class SummarizeResponse(BaseModel):
    original_text: str
    summary: str
    reduction_percentage: float


class ChatRequest(BaseModel):
    message: str
    context: Optional[str] = None


class ChatResponse(BaseModel):
    response: str
    model: str


@router.post("/sentiment", response_model=SentimentResponse)
async def analyze_sentiment(
    request: SentimentRequest,
    app_source: str = Depends(verify_api_key)
):
    """
    Analyze sentiment of text
    
    Uses Hugging Face transformer models
    """
    # TODO: Implement actual Hugging Face sentiment analysis
    # For now, return mock response
    
    text = request.text.lower()
    
    # Simple mock logic
    if any(word in text for word in ['excelente', 'genial', 'increíble', 'bueno']):
        sentiment = 'positive'
        score = 0.85
    elif any(word in text for word in ['malo', 'terrible', 'horrible', 'pésimo']):
        sentiment = 'negative'
        score = -0.75
    else:
        sentiment = 'neutral'
        score = 0.0
    
    return SentimentResponse(
        text=request.text,
        sentiment=sentiment,
        score=score,
        confidence=0.92
    )


@router.post("/summarize", response_model=SummarizeResponse)
async def summarize_text(
    request: SummarizeRequest,
    app_source: str = Depends(verify_api_key)
):
    """
    Summarize long text
    
    Uses Hugging Face summarization models
    """
    # TODO: Implement actual Hugging Face summarization
    original_length = len(request.text)
    
    # Mock summary
    summary = request.text[:request.max_length] + "..." if len(request.text) > request.max_length else request.text
    
    return SummarizeResponse(
        original_text=request.text,
        summary=summary,
        reduction_percentage=((original_length - len(summary)) / original_length) * 100 if original_length > 0 else 0
    )


@router.post("/chat", response_model=ChatResponse)
async def chat(
    request: ChatRequest,
    app_source: str = Depends(verify_api_key)
):
    """
    Chat with AI assistant
    
    Uses local LM Studio or Ollama based on config
    """
    import httpx
    from app.config import settings
    
    system_prompt = "Eres VRIS, el asistente inteligente de VerixRichon Factory. Responde de manera concisa y útil en español."
    
    try:
        if settings.MODEL_PROVIDER == "lm_studio":
            # LM Studio follows OpenAI API format
            async with httpx.AsyncClient(timeout=30.0) as client:
                payload = {
                    "messages": [
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": request.message}
                    ],
                    "temperature": 0.7,
                    "max_tokens": -1,
                    "stream": False
                }
                
                response = await client.post(
                    f"{settings.LM_STUDIO_URL}/chat/completions",
                    json=payload
                )
                
                if response.status_code != 200:
                    return ChatResponse(
                        response=f"Error conectando con LM Studio: {response.text}",
                        model="error"
                    )
                    
                data = response.json()
                content = data["choices"][0]["message"]["content"]
                model_id = data.get("model", "local-model")
                
                return ChatResponse(response=content, model=model_id)
                
            # Ollama API
            async with httpx.AsyncClient(timeout=30.0) as client:
                payload = {
                    "model": "llama3.1",  # Modelo descargado
                    "prompt": f"{system_prompt}\n\nUser: {request.message}\nAssistant:",
                    "stream": False
                }
                
                response = await client.post(
                    f"{settings.OLLAMA_URL}/generate",
                    json=payload
                )
                
                if response.status_code != 200:
                    return ChatResponse(
                        response=f"Error conectando con Ollama: {response.text}",
                        model="error"
                    )
                    
                data = response.json()
                content = data.get("response", "")
                
                return ChatResponse(response=content, model="ollama-model")
        
        else:
            return ChatResponse(
                response="Proveedor de modelo no configurado correctamente.",
                model="config-error"
            )
            
    except Exception as e:
        print(f"Error calling local LLM: {e}")
        # Fallback to mock if local model fails
        return ChatResponse(
            response="No pude conectar con mi cerebro local. ¿Está LM Studio/Ollama corriendo? (Respuesta de respaldo)",
            model="fallback-mock"
        )

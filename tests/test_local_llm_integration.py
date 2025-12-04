import pytest
from unittest.mock import AsyncMock, patch
from app.api.nlp import chat, ChatRequest, ChatResponse
from app.config import settings

@pytest.mark.asyncio
async def test_chat_lm_studio_integration():
    """Test chat endpoint with LM Studio provider"""
    # Setup
    settings.MODEL_PROVIDER = "lm_studio"
    settings.LM_STUDIO_URL = "http://localhost:1234/v1"
    
    mock_response_data = {
        "choices": [
            {
                "message": {
                    "content": "Hola, soy una IA local."
                }
            }
        ],
        "model": "local-model-v1"
    }
    
    # Mock httpx
    with patch("httpx.AsyncClient.post", new_callable=AsyncMock) as mock_post:
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = mock_response_data
        
        # Execute
        request = ChatRequest(message="Hola")
        # We pass a dummy string for the dependency
        response = await chat(request, app_source="valid-key")
        
        # Verify
        assert response.response == "Hola, soy una IA local."
        assert response.model == "local-model-v1"
        
        # Verify call arguments
        mock_post.assert_called_once()
        args, kwargs = mock_post.call_args
        assert kwargs["json"]["messages"][1]["content"] == "Hola"
        assert "http://localhost:1234/v1/chat/completions" in args[0]

@pytest.mark.asyncio
async def test_chat_ollama_integration():
    """Test chat endpoint with Ollama provider"""
    # Setup
    settings.MODEL_PROVIDER = "ollama"
    settings.OLLAMA_URL = "http://localhost:11434/api"
    
    mock_response_data = {
        "response": "Soy Ollama."
    }
    
    # Mock httpx
    with patch("httpx.AsyncClient.post", new_callable=AsyncMock) as mock_post:
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = mock_response_data
        
        # Execute
        request = ChatRequest(message="Hola Ollama")
        response = await chat(request, app_source="valid-key")
        
        # Verify
        assert response.response == "Soy Ollama."
        assert response.model == "ollama-model"
        
        # Verify call arguments
        mock_post.assert_called_once()
        args, kwargs = mock_post.call_args
        assert "User: Hola Ollama" in kwargs["json"]["prompt"]
        assert "http://localhost:11434/api/generate" in args[0]

@pytest.mark.asyncio
async def test_chat_fallback_error():
    """Test fallback when connection fails"""
    settings.MODEL_PROVIDER = "lm_studio"
    
    with patch("httpx.AsyncClient.post", new_callable=AsyncMock) as mock_post:
        # Simulate exception
        mock_post.side_effect = Exception("Connection refused")
        
        request = ChatRequest(message="Hola")
        response = await chat(request, app_source="valid-key")
        
        assert "No pude conectar" in response.response
        assert response.model == "fallback-mock"

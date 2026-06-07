from fastapi import APIRouter, WebSocket
from app.websocket.handler import websocket_handler

router = APIRouter()

@router.websocket("/ws/{conversation_id}")
async def websocket_endpoint(websocket: WebSocket, conversation_id: str):
    await websocket_handler(websocket, conversation_id)


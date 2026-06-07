import asyncio
from fastapi import WebSocket, WebSocketDisconnect
from redis.asyncio import Redis

from app.websocket.manager import manager
from app.config import settings



async def websocket_handler(websocket: WebSocket, conversation_id: str):
    redis = Redis.from_url(settings.REDIS_URL)

    await manager.connection(websocket, conversation_id)

    listen_task = asyncio.create_task(
        manager.listen(redis, conversation_id)
    )

    try:
        while True:
            data = await websocket.receive_json()

            data['conversation_id'] = conversation_id

            await manager.publish(redis, conversation_id, data)
    
    except WebSocketDisconnect:

        await manager.disconnect(websocket, conversation_id)

        listen_task.cancel()

        await redis.aclose()
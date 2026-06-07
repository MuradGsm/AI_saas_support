import json
from fastapi import WebSocket
from redis.asyncio import Redis


class ConnectionManager:
    def __init__(self):
        self.connections: dict[str, list[WebSocket]] = {}

    
    async def connection(self, websocket: WebSocket, conversation_id: str):
        await websocket.accept()

        if conversation_id not in self.connections:
            self.connections[conversation_id] = []
        
        self.connections[conversation_id].append(websocket)

    async def disconnect(self, websocker: WebSocket, conversation_id: str):
        if conversation_id in self.connections:
            self.connections[conversation_id].remove(websocker)
        
            if not self.connections[conversation_id]:
                del self.connections[conversation_id]
    
    async def broadcast(self, conversation_id: str, message: dict):
        connections = self.connections.get(conversation_id)

        for websocket in connections:
            try:
                await websocket.send_json(message)
            except Exception:
                pass
    
    async def publish(self, redis: Redis, conversation_id: str, message: dict):
        await redis.publish(
            f"conv:{conversation_id}",
            json.dumps(message)
        )
    
    async def listen(self, redis: Redis, conversation_id: str):
        pubsub = redis.pubsub()
        await pubsub.subscribe(f"conv:{conversation_id}")

        async for msg in pubsub.listen():
            if msg['type'] == 'message':
                data = json.loads(msg['data'])
                await self.broadcast(conversation_id, data)

manager = ConnectionManager()


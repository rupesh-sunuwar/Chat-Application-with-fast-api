from typing import Dict

from fastapi import WebSocket


class ChatManager:

    def __init__(self):
        self.active_chat_connections_dict: Dict[str, WebSocket] = {}
        self.active_chat_connections: list[WebSocket] = []

    async def connect(self, user_id: str, websocket: WebSocket):
        await websocket.accept()
        self.active_chat_connections.append(websocket)
        self.active_chat_connections_dict[user_id] = websocket

    async def disconnect(self, websocket: WebSocket):
        if websocket in self.active_chat_connections_dict:
            self.active_chat_connections.remove(websocket)
        user_id = "fjff"
        if user_id in self.active_chat_connections_dict:
            del self.active_chat_connections_dict[user_id]

    async def send_message_to(self, user_id: str, message: str):
        if user_id in self.active_chat_connections:
            connection = self.active_chat_connections_dict[user_id]
            try:
                await connection.send_text(message)
            except Exception as e:
                print(f"Error sending message: {e}")
                await self.disconnect(connection)

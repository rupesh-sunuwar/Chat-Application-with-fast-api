from datetime import datetime
from typing import List, Literal

from bson import ObjectId
from odmantic import Model, EmbeddedModel


class Users(Model):
    first_name: str
    last_name: str
    username: str
    password: str
    email: str


class Participant(EmbeddedModel):
    user_id: ObjectId
    joined_at: datetime


class ChatRoom(Model):
    name: str
    is_group: bool
    participants: List[Participant]
    created_at: datetime
    updated_at: datetime
    last_message_id: ObjectId



class Message(Model):
    chat_room_id: ObjectId
    sender_id: ObjectId
    message: str
    sent_at: datetime
    message_type: Literal["text", "image", "video", "file"]
    status: Literal["sent", "delivered", "read"]


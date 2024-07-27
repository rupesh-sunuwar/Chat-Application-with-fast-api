from pydantic import BaseModel


class UserResponse(BaseModel):
    full_name: str
    email: str
    id: str

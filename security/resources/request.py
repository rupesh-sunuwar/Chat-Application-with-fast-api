from pydantic import BaseModel


class LoginRequest(BaseModel):
    username: str
    password: str


class UserRequest(BaseModel):
    first_name: str
    last_name: str
    username: str
    password: str
    email: str


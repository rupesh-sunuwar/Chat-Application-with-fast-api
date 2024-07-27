from typing import Optional

from fastapi import HTTPException, Request
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'], deprecated="auto")


class AuthUtil:
    def __init__(self, request: Request):
        self.request = request
        if not hasattr(request.state, 'user'):
            from starlette import status
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )
        self.token_data = request.state.user

    def get_username(self) -> Optional[str]:
        if self.token_data:
            return self.token_data.email
        return None

    def get_user_id(self) -> Optional[str]:
        if self.token_data:
            return self.token_data.encrypted_id
        return None

    def get_roles(self) -> Optional[list]:
        if self.token_data:
            return self.token_data.roles
        return None

    def get_permissions(self) -> Optional[list]:
        if self.token_data:
            return self.token_data.permissions
        return None

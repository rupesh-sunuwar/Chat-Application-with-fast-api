import base64

from odmantic import AIOEngine

from exception.auth_exception import InvalidAuthenticationException
from security.repository.user_repository import UserRepository
from security.resources.request import LoginRequest
from security.util.hasing import Hash


class AuthenticationService:
    def __init__(self, db: AIOEngine):
        self.db = db

    async def login_user(self, login_request: LoginRequest):
        print("Logging the user")
        user = await UserRepository.get_user(self.db, login_request.username)
        print(user)
        if not user:
            raise InvalidAuthenticationException("Invalid credential")
        if not Hash.verify(user.password, login_request.password):
            raise InvalidAuthenticationException("Incorrect password")
        return user



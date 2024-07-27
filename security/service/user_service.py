from fastapi import HTTPException
from odmantic import AIOEngine

from exception.custom_exception import ClientException
from security.model.model import Users
from security.repository.user_repository import UserRepository
from security.resources.request import UserRequest
from security.resources.response import UserResponse
from security.util.auth_util import pwd_context


class UserService:

    def __init__(self, db: AIOEngine):
        self.db = db

    @staticmethod
    async def get_user(db: AIOEngine, username: str):
        try:
            db_user = await UserRepository.get_user(db, username)
            if db_user is None:
                raise HTTPException(status_code=404, detail="User not found")
            return UserResponse(**db_user)
        except Exception as e:
            raise HTTPException(status_code=404, detail=str(e))

    @staticmethod
    async def get_user_by_email(db: AIOEngine, email: str):
        try:
            db_user = await UserRepository.get_user_by_email(db, email)
            if db_user is None:
                raise HTTPException(status_code=404, detail="User not found")
            return UserResponse(**db_user)
        except Exception as e:
            raise HTTPException(status_code=404, detail=str(e))

    async def register_user(self, user: UserRequest):
        await self._throw_error_if_user_already_exist(self.db, user)
        print("user doesnt exist")

        hashed_password = pwd_context.hash(user.password)
        print("Hashed", hashed_password)
        new_user = Users(first_name=user.first_name, last_name=user.last_name, email=user.email,
                         username=user.username,
                         password=hashed_password)
        print(new_user)
        return await UserRepository.create_user(self.db, new_user)

    @staticmethod
    async def _throw_error_if_user_already_exist(db, user):
        print("user")
        db_user = await UserRepository.get_user(db, user.username)
        if db_user:
            raise ClientException("Username already registered", "00")

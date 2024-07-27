from fastapi import Depends, APIRouter

from di.dependencies import get_users_service
from security.resources.request import UserRequest
from security.service.user_service import UserService

router = APIRouter(tags=['User Controller'])


@router.post("/register_user")
async def register_user(user: UserRequest,
                        service: UserService =
                        Depends(get_users_service)):
    return await service.register_user(user)



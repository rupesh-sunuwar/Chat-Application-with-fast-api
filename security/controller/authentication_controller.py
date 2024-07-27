from fastapi import APIRouter, Depends

from di.dependencies import get_auth_service
from security.resources.request import LoginRequest
from security.service.authentication_service import AuthenticationService

router = APIRouter(tags=['Auth Controller'])


@router.post('/login')
async def login(login_request: LoginRequest, auth_service: AuthenticationService = Depends(get_auth_service)):
    return await auth_service.login_user(login_request)

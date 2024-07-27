from config.database import engine
from security.service.authentication_service import AuthenticationService
from security.service.user_service import UserService


def get_auth_service():
    return AuthenticationService(engine)


def get_users_service():
    return UserService(engine)

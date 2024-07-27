from fastapi import HTTPException


class InvalidAuthenticationException(HTTPException):
    def __init__(self, detail: str, code: str = "33"):
        detail = {
            "code": code,
            "message": detail,
            "data": {}
        }
        super().__init__(status_code=400, detail=detail)

from fastapi import HTTPException


class ClientException(HTTPException):

    def __init__(self, detail: str, code: str):
        detail = {
            "code": code,
            "message": detail,
            "data": {}
        }
        super().__init__(status_code=400, detail=detail)
       
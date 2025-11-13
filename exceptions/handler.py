# exceptions/handlers.py
from fastapi import Request, status
from fastapi.exceptions import RequestValidationError

from exceptions.user_errors import USER_VALUE_ERROR_MAP, USER_VALIDATION_ERROR_MAP
from exceptions.post_erros import POST_VALUE_ERROR_MAP, POST_VALIDATION_ERROR_MAP
from exceptions.coment_erros import COMMENT_VALUE_ERROR_MAP
from utils.formatter import create_json_response


# ValueError
VALUE_ERROR_MAP = {
    **USER_VALUE_ERROR_MAP,
    **POST_VALUE_ERROR_MAP,
    **COMMENT_VALUE_ERROR_MAP
}

# RequestValidationError
VALIDATION_ERROR_MAP = {
    **USER_VALIDATION_ERROR_MAP,
    **POST_VALIDATION_ERROR_MAP
}


# ValueError 처리
async def value_error_exception_handler(request: Request, exc: ValueError):
    msg = str(exc)
    print("🔥 ValueError:", msg)

    for key, (status_code, message) in VALUE_ERROR_MAP.items():
        if key in msg:  
            return create_json_response(status_code, message)
        
    return create_json_response(status.HTTP_400_BAD_REQUEST, "invalid_request")


# 요청 데이터 유효성 검증 실패 처리
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    for error in exc.errors():
        msg = error.get("msg")
        print("🔥 Validation Error:", msg)

        for key, message in VALIDATION_ERROR_MAP.items():
            if key in msg:
                return create_json_response(status.HTTP_422_UNPROCESSABLE_ENTITY, message)
        
        return create_json_response(status.HTTP_422_UNPROCESSABLE_ENTITY, "invalid_request")


# 예상치 못한 서버 내부 오류 처리
async def server_exception_handler(request: Request, exc: Exception):
    return create_json_response(status.HTTP_500_INTERNAL_SERVER_ERROR, "internal_server_error")


# exceptions/handlers.py
from fastapi import Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse


async def validation_exception_handler(request: Request, exc: RequestValidationError):
    for error in exc.errors():
        field = error["loc"][-1]
        msg = error.get("msg")

        # 이메일 형식 불일치
        if field == "email":
            return JSONResponse(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                content={
                    "message": "*올바른 이메일 주소 형식을 입력해주세요.",
                    "data": None
                }
            )

        # 비밀번호 미입력
        if msg == "password_required":
            return JSONResponse(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                content={
                    "message": "*비밀번호를 입력해주세요.", 
                    "data": None
                }
            )
        
        # 비밀번호 규칙 실패
        if msg == "invalid_password_rule":
            return JSONResponse(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                content={
                    "message": "*비밀번호는 8자 이상, 20자 이하이며, 대문자, 소문자, 숫자, 특수문자를 각각 최소 1개 포함해야 합니다.",
                    "data": None
                }
            )
        
    # 그 외 에러
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "message": "invalid_request",
            "data": None
        }
    )
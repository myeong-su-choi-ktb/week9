# exceptions/handlers.py
from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse


# 사용자 로그인 및 회원가입 요청 시 발생하는 RequestValidationError를 처리하는 함수
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    for error in exc.errors():
        field = error["loc"][-1]
        msg = error.get("msg")

        # 비밀번호가 입력되지 않은 경우
        if "password_required" in msg:
            return JSONResponse(
                status_code=422,
                content={
                    "message": "*비밀번호를 입력해주세요.",
                    "data": None
                }
            )
        
        # 이메일 형식이 올바르지 않은 경우
        if field == "email":
            return JSONResponse(
                status_code=422, 
                content={
                        "message": "*올바른 이메일 형식을 입력해주세요.",
                        "data": None
                    }
                )

        # 비밀번호 규칙 검증 실패 시
        if field == "password" or msg == "invalid_password_rule":
            return JSONResponse(
                status_code=422,
                content={
                    "message": "*비밀번호는 8자 이상, 20자 이하이며, 대문자, 소문자, 숫자, 특수문자를 각각 최소 1개 포함해야 합니다.",
                    "data": None,
                },
            )

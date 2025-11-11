from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError

from routers.user_router import router as user_router
from exceptions.user_exception import validation_exception_handler


# FastAPI 애플리케이션 생성
app = FastAPI()

# 사용자 관련 라우터 등록
app.include_router(user_router)

# Request body 검증 실패 시 실행될 예외 처리 핸들러 등록
app.add_exception_handler(RequestValidationError, validation_exception_handler)
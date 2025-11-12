from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError

from routers.user_router import router as user_router
from exceptions.handler import *


# FastAPI 애플리케이션 생성
app = FastAPI()

# 라우터 등록
app.include_router(user_router)

# 예외 처리 등록
app.add_exception_handler(Exception, server_exception_handler)
app.add_exception_handler(ValueError, value_error_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
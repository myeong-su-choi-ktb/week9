# main.py
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError

from routers.user_router import router as user_router
from routers.post_router import router as post_router
from routers.comment_router import router as comment_router
from exceptions.handler import server_exception_handler, value_error_exception_handler, validation_exception_handler


# FastAPI 애플리케이션 생성
app = FastAPI()

# 라우터 등록
app.include_router(user_router)
app.include_router(post_router)
app.include_router(comment_router)

# 예외 처리 등록
app.add_exception_handler(Exception, server_exception_handler)
app.add_exception_handler(ValueError, value_error_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
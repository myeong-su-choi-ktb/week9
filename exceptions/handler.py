# exceptions/handlers.py
from fastapi import Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse


# 서버 내부 오류 발생 시
async def server_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "message": "internal_server_error",
            "data": None
        }
    )

# ValueError 처리
async def value_error_exception_handler(request: Request, exc: ValueError):
    msg = str(exc)

    print("🔥 Value error:", msg)

    if "user_not_found" in msg:
        return JSONResponse(
            status_code=404, 
            content={"message": "*존재하지 않는 사용자입니다.", 
                     "data": None
                }
            )

# 요청 데이터 유효성 검증 실패 시
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    for error in exc.errors():
        print("🔥 Validation Errors:", error)

        msg = error.get("msg")

        # 이메일 형식이 유효하지 않은 경우
        if "value is not a valid email address" in msg:
            return JSONResponse(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                content={
                    "message": "*올바른 이메일 주소 형식을 입력해주세요.",
                    "data": None
                }
            )

        # 이메일이 비어 있는 경우
        if "email_required" in msg:
            return JSONResponse(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                content={
                    "message": "*이메일을 입력해주세요.",
                    "data": None
                }
            )

        # 비밀번호 입력 안했을 시
        if "password_required" in msg:
            return JSONResponse(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                content={
                    "message": "*비밀번호를 입력해주세요.", 
                    "data": None
                }
            )
        
        # 비밀번호 확인 유효성을 통과 못하였을 경우
        if "invalid_password_rule" in msg:
            return JSONResponse(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                content={
                    "message": "*비밀번호는 8자 이상, 20자 이하이며, 대문자, 소문자, 숫자, 특수문자를 각각 최소 1개 포함해야 합니다.",
                    "data": None
                }
            )
        
        # 비밀번호 확인 입력 안했을 시
        if "password_confirm_required" in msg:
            return JSONResponse(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                content={
                    "message": "*비밀번호를 한번더 입력해주세요.",
                    "data": None
                }
            )
        
        # 비밀번호 확인과 다를 시
        if "password_not_match" in msg:
            return JSONResponse(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                content={
                    "message": "*비밀번호가 다릅니다.",
                    "data": None
                }
            )
        
        # 프로필 이미지 검증 실패
        if "profile_image_required" in msg:
            return JSONResponse(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                content={
                    "message": "*프로필 사진을 추가해주세요.",
                    "data": None
                }
            )
        
        # 닉네임 입력하지 않을 시
        if "nickname_required" in msg:
            return JSONResponse(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                content={
                    "message": "*닉네임을 입력해주세요.",
                    "data": None
                }
            )
        
        # 닉네임 띄어쓰기 불가
        if "nickname_no_space" in msg:
            return JSONResponse(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                content={
                    "message": "*띄어쓰기를 없애주세요.",
                    "data": None
                }
            )
        
        # 닉네임 10글자 이내
        if "nickname_max_length" in msg:
            return JSONResponse(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                content={
                    "message": "*닉네임은 최대 10자 까지 작성 가능합니다.",
                    "data": None
                }
            )
        
        # 사용자를 찾지 못한 경우
        if "user_not_found" in msg:
            return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND,
                content={
                    "message": "*존재하지 않는 사용자입니다.",
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
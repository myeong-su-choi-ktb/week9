# utils/formatter.py
from fastapi.responses import JSONResponse


# 좋아요, 댓글, 조회 숫자 포멧팅
def format_number(value: int) -> str:
    if value >= 100000:
        return f"{value // 1000}k"
    if value >= 10000:
        return f"{value // 1000}k"
    if value >= 1000:
        return f"{value // 1000}k"
    return str(value)

# JSON Response 포맷
def create_json_response(status_code: int, message: str, data=None) -> JSONResponse:
    return JSONResponse(
        status_code=status_code,
        content={"message": message, "data": data}
    )
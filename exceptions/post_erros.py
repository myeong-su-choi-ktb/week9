# exceptions/post_errors.py
from fastapi import status

# ValueError
POST_VALUE_ERROR_MAP = {
    "post_not_found": (status.HTTP_404_NOT_FOUND, "*존재하지 않는 게시글입니다."),
}

# RequestValidationError
POST_VALIDATION_ERROR_MAP = {
    "title_and_content_required": "*제목, 내용을 모두 작성해주세요.",
    "title_too_long": "*제목은 26자 이내로 작성해주세요."
}
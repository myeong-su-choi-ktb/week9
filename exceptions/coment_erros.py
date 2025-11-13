# exceptions/comment_errors.py
from fastapi import status


COMMENT_VALUE_ERROR_MAP = {
    "permission_denied": (status.HTTP_403_FORBIDDEN, "*권한이 없습니다."),
    "comment_not_found": (status.HTTP_404_NOT_FOUND, "*존재하지 않는 댓글입니다.")
}
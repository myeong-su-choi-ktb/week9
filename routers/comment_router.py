# routers/comment_router.py
from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from models.comment_model import CommentCreate, CommentUpdate
from controllers.comment_controller import create_comment_service, update_comment_service, delete_comment_service
from utils.formatter import create_json_response


router = APIRouter(prefix="/comments")

# 댓글 생성 API
@router.post("/posts/{post_id}")    # http://127.0.0.1:8000/comments/posts/1?author_id=3
async def create_comment(post_id: int, author_id: int, comment_dto: CommentCreate) -> JSONResponse:
    data = await create_comment_service(post_id, author_id, comment_dto)
    return create_json_response(status_code=status.HTTP_201_CREATED, message="댓글 작성 성공", data=data)


# 댓글 수정 API
@router.patch("/{comment_id}")      # http://127.0.0.1:8000/comments/1?author_id=1
async def update_comment(comment_id: int, author_id: int, comment_dto: CommentUpdate) -> JSONResponse:
    data = await update_comment_service(comment_id, author_id, comment_dto)
    return create_json_response(status_code=status.HTTP_200_OK, message="댓글 수정 성공", data=data)


# 댓글 삭제 API
@router.delete("/{comment_id}")     # http://127.0.0.1:8000/comments/6
async def delete_comment(comment_id: int, author_id: int) -> JSONResponse:
    data = await delete_comment_service(comment_id, author_id)
    return create_json_response(status_code=status.HTTP_200_OK, message="댓글 삭제 성공", data=data)
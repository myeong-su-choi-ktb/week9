# routers/post_router.py
from fastapi import APIRouter, Query, status
from fastapi.responses import JSONResponse

from models.post_model import PostCreate
from controllers.post_controller import get_post_list_service, get_post_detail_service, delete_post_service, toogle_post_like_service, create_post_service
from utils.formatter import create_json_response


router = APIRouter(prefix="/posts")


# 게시글 생성 API
@router.post("")
async def create_post(post_dto: PostCreate) -> JSONResponse:
    data = await create_post_service(post_dto)
    return create_json_response(status_code=status.HTTP_201_CREATED, message="게시글 생성 성공", data=data)


# 게시글 목록 조회 API
@router.get("") 
async def get_post_list(limit: int = Query(20), offset: int = Query(0)) -> JSONResponse:
    data = await get_post_list_service(limit, offset)
    return create_json_response(status_code=status.HTTP_200_OK, message="게시글 목록 조회 성공", data=data)


# 게시글 상세 조회 API
@router.get("/{post_id}")
async def get_post_detail(post_id: int) -> JSONResponse:
    data = await get_post_detail_service(post_id)
    return create_json_response(status_code=status.HTTP_200_OK, message="게시글 상세 조회 성공", data=data)


# 게시글 삭제 API
@router.delete("/{post_id}")
async def delete_post(post_id: int) -> JSONResponse:
    data = await delete_post_service(post_id)
    return create_json_response(status_code=status.HTTP_200_OK, message="게시글 삭제 성공", data=data)


# 좋아요 토클 API
@router.post("/{post_id}/like")
async def toggle_post_like(post_id: int, user_id: int) -> JSONResponse:
    data = await toogle_post_like_service(post_id, user_id)
    return create_json_response(status_code=status.HTTP_200_OK, message="좋아요 토클 성공", data=data)
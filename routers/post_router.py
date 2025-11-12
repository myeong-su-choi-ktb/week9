from fastapi import APIRouter, Query
from models.post_model import *
from controllers.post_controller import *


router = APIRouter(prefix="/posts")

# 게시글 목록 조회 API
@router.get("", response_model=List[PostListItem])
def get_post_list(limit: int = Query(20), offset: int = Query(0)):
    return get_posts(limit, offset)
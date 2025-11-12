# models/post_model.py
from pydantic import BaseModel
from typing import Optional, List, Dict
from datetime import datetime   # test용


# 사용자 정보 in-memory 저장소
posts: List[Dict] = [
    {"id": 1, "author_id": 1, "title": "첫 번째 게시글 제목입니다.", "contnet": "첫 번째 게시글 내용입니다.", "like_count": 1000, "view_count": 0, "comment_count":0, "create_at": datetime.now(), "updated_at": datetime.now()},
    {"id": 2, "author_id": 2, "title": "두 번째 게시글 제목입니다.", "contnet": "두 번째 게시글 내용입니다.", "like_count": 10000, "view_count": 0, "comment_count":0, "create_at": datetime.now(), "updated_at": datetime.now()},
    {"id": 3, "author_id": 3, "title": "세 번째 게시글 제목입니다.", "contnet": "세 번째 게시글 내용입니다.", "like_count": 100000, "view_count": 0, "comment_count":0, "create_at": datetime.now(), "updated_at": datetime.now()},
    {"id": 4, "author_id": 4, "title": "네 번째 게시글 제목입니다.", "contnet": "네 번째 게시글 내용입니다.", "like_count": 0, "view_count": 100000, "comment_count": 1000, "create_at": datetime.now(), "updated_at": datetime.now()},
    {"id": 5, "author_id": 5, "title": "다섯 번째 게시글 제목입니다.", "contnet": "첫 번째 게시글 내용입니다.", "like_count": 0, "view_count": 10000, "comment_count":0, "create_at": datetime.now(), "updated_at": datetime.now()},
    {"id": 6, "author_id": 1, "title": "여섯 번째 게시글 제목입니다. 26글자가 넘어가게 해보겠습니다. 한번 더 타이핑 하겠습니다.", "contnet": "다섯 번째 게시글 내용입니다.", "like_count": 0, "view_count": 0, "comment_count":0, "create_at": datetime.now(), "updated_at": datetime.now()}
]


""" ----------------------------- 게시글 목록 조회 관련 ----------------------------- """

# 게시글 목록 응답 DTO
class PostListItem(BaseModel):
    id: int
    author_id: int
    title: str
    view_count: str
    like_count: str
    comment_count: str
    updated_at: str



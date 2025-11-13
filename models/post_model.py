# models/post_model.py
from pydantic import BaseModel, field_validator
from typing import List, Dict, Optional
from datetime import datetime, timedelta
from validators.post_validator import validate_not_empty, validate_title_length


# 게시글 정보를 임시로 저장하는 in-memory 저장소
now = datetime.now()
posts: List[Dict] = [
    {"id": 1, "author_id": 1, "title": "첫 번째 게시글 제목입니다.", "content": "첫 번째 게시글 내용입니다.", "image_url": "https://image.com/post1.png", "like_count": 1000, "view_count": 0, "comment_count": 0, "created_at": now - timedelta(days=5), "updated_at": now - timedelta(days=4)},
    {"id": 2, "author_id": 2, "title": "두 번째 게시글 제목입니다.", "content": "두 번째 게시글 내용입니다.", "like_count": 10000, "view_count": 0, "comment_count": 0, "created_at": now - timedelta(days=4, hours=2), "updated_at": now - timedelta(days=3, hours=1)},
    {"id": 3, "author_id": 3, "title": "세 번째 게시글 제목입니다.", "content": "세 번째 게시글 내용입니다.", "like_count": 100000, "view_count": 0, "comment_count": 0, "created_at": now - timedelta(days=3), "updated_at": now - timedelta(days=2, minutes=30)},
    {"id": 4, "author_id": 4, "title": "네 번째 게시글 제목입니다.", "content": "네 번째 게시글 내용입니다.", "image_url": "https://image.com/post4.png", "like_count": 0, "view_count": 100000, "comment_count": 1000, "created_at": now - timedelta(days=2), "updated_at": now - timedelta(days=1)},
    {"id": 5, "author_id": 5, "title": "다섯 번째 게시글 제목입니다.", "content": "첫 번째 게시글 내용입니다.", "like_count": 0, "view_count": 10000, "comment_count": 0, "created_at": now - timedelta(hours=10), "updated_at": now - timedelta(hours=6)},
    {"id": 6, "author_id": 1, "title": "여섯 번째 게시글 제목입니다. 26글자가 넘어가게 해보겠습니다. 한번 더 타이핑 하겠습니다.", "content": "다섯 번째 게시글 내용입니다.", "like_count": 0, "view_count": 0, "comment_count": 0, "created_at": now - timedelta(minutes=20), "updated_at": now}
]

# 게시글 좋아요 수를 저장하는 in-memory 저장소
liked_posts: List[Dict] = [
    {"post_id": 1, "user_id": 1},
    {"post_id": 1, "user_id": 3},
    {"post_id": 1, "user_id": 4},
    {"post_id": 2, "user_id": 1},
    {"post_id": 3, "user_id": 1},
    {"post_id": 4, "user_id": 1},
    {"post_id": 4, "user_id": 5},
    {"post_id": 4, "user_id": 2}
]

# 게시글 생성 요청 DTO
class PostCreate(BaseModel):
    author_id: int
    title: str
    content: str
    image_url: Optional[str] = None

    # 제목과 내용이 비어있는지 검사
    @field_validator("title", "content")
    @classmethod
    def check_not_empty(cls, value):
        return validate_not_empty(value)
    
    # 제목 길이 제한
    @field_validator("title")
    @classmethod
    def title_length_validator(cls, value):
        return validate_title_length(value)
    
    
# 게시글 수정 요청 DTO
class PostUpdate(BaseModel):
    title: str
    content: str
    image_url: Optional[str] = None

    # 제목과 내용이 비어있는지 검사
    @field_validator("title", "content")
    @classmethod
    def check_not_empty(cls, value):
        return validate_not_empty(value)
    
    # 제목 길이 제한
    @field_validator("title")
    @classmethod
    def title_length_validator(cls, value):
        return validate_title_length(value)

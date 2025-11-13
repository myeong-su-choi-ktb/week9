# models/comment_model.py
from typing import List, Dict
from datetime import datetime, timedelta
from pydantic import BaseModel


# 댓글 정보를 임시로 저장하는 in-memory 저장소
now = datetime.now()
comments: List[Dict] = [
    {"id": 1, "post_id": 1, "author_id": 1, "content": "테스트1 댓글입니다.", "created_at": now - timedelta(days=5, hours=1), "updated_at": now - timedelta(days=5)},
    {"id": 2, "post_id": 1, "author_id": 3, "content": "테스트2 댓글입니다.", "created_at": now - timedelta(days=3, hours=3), "updated_at": now - timedelta(days=3, hours=2)},
    {"id": 3, "post_id": 3, "author_id": 4, "content": "테스트3 댓글입니다.", "created_at": now - timedelta(days=2), "updated_at": now - timedelta(days=1, hours=3)},
    {"id": 4, "post_id": 4, "author_id": 2, "content": "테스트4 댓글입니다.", "created_at": now - timedelta(hours=10), "updated_at": now - timedelta(hours=5)},
    {"id": 5, "post_id": 2, "author_id": 1, "content": "테스트5 댓글입니다.", "created_at": now - timedelta(minutes=20), "updated_at": now}
]

# 댓글 생성 요청 DTO
class CommentCreate(BaseModel):
    content: str

# 댓글 수정 요청 DTO
class CommentUpdate(BaseModel):
    content: str
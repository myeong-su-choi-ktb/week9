# controllers/comment_controller.py
from datetime import datetime
from models.comment_model import comments # DB 대체
from models.comment_model import CommentCreate, CommentUpdate
from models.post_model import posts # DB 대체


# 댓글 작성 서비스
async def create_comment_service(post_id: int, author_id: int, comment_dto: CommentCreate) -> dict:

    # 게시글 존재 여부 확인
    post = next((p for p in posts if p["id"] == post_id), None)
    if not post:
        raise ValueError("post_not_found")
    
    # 댓글 ID 자동 증가
    next_id = max([c["id"] for c in comments]) + 1 if comments else 1

    new_comment = {
        "id": next_id,
        "post_id": post_id,
        "author_id": author_id,
        "content": comment_dto.content,
        "created_at": datetime.now(),
        "updated_at": datetime.now()
    }

    comments.append(new_comment)

    # 게시글 댓글 수 증가
    post["comment_count"] += 1

    return {
        **new_comment,
        "created_at": new_comment["created_at"].strftime("%Y-%m-%d %H:%M:%S"),
        "updated_at": new_comment["updated_at"].strftime("%Y-%m-%d %H:%M:%S")
    }


# 댓글 수정 서비스
async def update_comment_service(comment_id: int, author_id: int, comment_dto: CommentUpdate) -> dict:

    # 수정 대상 댓글 조회
    target = next((c for c in comments if c["id"] == comment_id), None)
    if not target:
        raise ValueError("comment_not_found")
    
    # 작성자 본인 확인
    if target["author_id"] != author_id:
        raise ValueError("permission_denied")

    # 내용 수정
    target["content"] = comment_dto.content
    target["updated_at"] = datetime.now()

    return {
        "id": target["id"],
        "post_id": target["post_id"],
        "author_id": target["author_id"],
        "content": target["content"],
        "updated_at": target["updated_at"].strftime("%Y-%m-%d %H:%M:%S"),
    }


# 댓글 삭제 서비스
async def delete_comment_service(comment_id: int, author_id: int) -> dict:

    # 삭제 대상 댓글 조회
    target = next((c for c in comments if c["id"] == comment_id), None)
    if not target:
        raise ValueError("comment_not_found")
    
    # 작성자 본인 확인
    if target["author_id"] != author_id:
        raise ValueError("permission_denied")

    # 해당 게시글 댓글 수 감소
    post = next((p for p in posts if p["id"] == target["post_id"]), None)
    if not post:
        raise ValueError("post_not_found")
    post["comment_count"] = max(0, post["comment_count"] - 1)

    # 댓글 삭제
    comments.remove(target)

    return { 
        "id": comment_id 
    }

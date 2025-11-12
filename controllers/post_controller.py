# controllers/post_controller.py
from fastapi import status
from fastapi.responses import JSONResponse

from models.post_model import PostCreate
from models.post_model import posts, liked_posts # DB 대체
from models.comment_model import comments # DB 대체
from utils.formatter import format_number

from datetime import datetime



# 게시글 생성 서비스
async def create_post_service(post_dto: PostCreate) -> dict:

    # ID 자동 증가
    next_id = max([p["id"] for p in posts]) + 1 if posts else 1

    new_post = {
        "id": next_id,
        "author_id": post_dto.author_id,
        "title": post_dto.title,
        "content": post_dto.content,
        "image_url": post_dto.image_url,
        "like_count": 0,
        "view_count": 0,
        "comment_count": 0,
        "create_at": datetime.now(),
        "updated_at": datetime.now()
    }

    posts.append(new_post)

    return {
        **new_post,
        "create_at": new_post["create_at"].strftime("%Y-%m-%d %H:%M:%S"),
        "updated_at": new_post["updated_at"].strftime("%Y-%m-%d %H:%M:%S"),
    }


# 게시글 목록 조회 서비스
async def get_post_list_service(limit: int, offset: int) -> dict:

    # 요청 범위에 맞는 게시글을 잘라서 가져오기
    slice_posts = posts[offset: offset + limit]

    return [
        {
            "id": post["id"],
            "author_id": post["author_id"],
            "title": post["title"][:26],                        # 제목 길이 제한
            "view_count": format_number(post["view_count"]),    # 숫자 포맷 적용 (1k 등)
            "like_count": format_number(post["like_count"]),
            "comment_count": format_number(post["comment_count"]),
            "updated_at": post["updated_at"].strftime("%Y-%m-%d %H:%M:%S")
        }
        for post in slice_posts
    ]


# 게시글 상세 조회 서비스
async def get_post_detail_service(post_id: int) -> dict:

    # 게시글 찾기
    post = next((p for p in posts if p["id"] == post_id), None)
    if not post:
        raise ValueError("post_not_found")
    
    # 조회수 증가
    post["view_count"] += 1

    # 댓글 리스트 생성
    comment_list = [
        {
            "id": c["id"],
            "author_id": c["author_id"],
            "content": c["content"],
            "updated_at": c["updated_at"].strftime("%Y-%m-%d %H:%M:%S")
        }
        for c in comments if c["post_id"] == post_id
    ]

    return {
        "id": post["id"],
        "author_id": post["author_id"],
        "title": post["title"],
        "content": post["content"],
        "view_count": format_number(post["view_count"]),
        "like_count": format_number(post["like_count"]),
        "comment_count": format_number(post["comment_count"]),
        "updated_at": post["updated_at"].strftime("%Y-%m-%d %H:%M:%S"),
        "image_url": post.get("image_url"),      # optional
        "comments": comment_list
    }
    

# 게시글 삭제 서비스
async def delete_post_service(post_id: int) -> dict:

    # 게시글 찾기
    post = next((p for p in posts if p["id"] == post_id), None)
    if not post:
        raise ValueError("post_not_found")
    
    # 게시글 삭제
    posts.remove(post)

    # 해당 게시글의 모든 댓글 삭제
    comments[:] = [c for c in comments if c["post_id"] != post_id]

    return {
        "id": post_id
    }
    

# 게시글 좋아요 토글 서비스
async def toogle_post_like_service(post_id: int, user_id: int) -> dict:
    
    # 이미 좋아요 눌렀는지 검색
    like = next((item for item in liked_posts if item["post_id"] == post_id and item["user_id"] == user_id), None)

    # 게시글 객체 가져오기
    post = next((p for p in posts if p["id"] == post_id), None)
    if not post:
        raise ValueError("post_not_found")
    
    if like:
        # 좋아요 취소
        liked_posts.remove(like)
        post["like_count"] -= 1
        
        return {
            "action": "unliked",
            "like_count": post["like_count"]
        }

    else:
        # 좋아요 추가
        liked_posts.append({"post_id": post_id, "user_id": user_id})
        post["like_count"] += 1
        
        return {
            "action": "liked",
            "like_count": post["like_count"]
        }
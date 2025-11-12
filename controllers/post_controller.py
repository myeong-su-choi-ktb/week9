from models.post_model import *


# 게시글 목록 조회 서비스
def get_posts(limit: int, offset: int):
    slice_posts = posts[offset: offset + limit]

    result = []
    for post in slice_posts:
        result.append(
            PostListItem(
                id=post["id"],
                author_id=post["author_id"],
                title=post["title"][:26],
                view_count=format_number(post["view_count"]),
                like_count=format_number(post["like_count"]),
                comment_count=format_number(post["comment_count"]),
                updated_at=post["updated_at"].strftime("%Y-%m-%d %H:%M:%S")
            )
        )

    return result

# 숫자 표기 규칙 (1k, 10k, 100k)
def format_number(value: int) -> str:
    if value >= 100000:
        return f"{value // 1000}k"
    if value >= 10000:
        return f"{value // 1000}k"
    if value >= 1000:
        return f"{value // 1000}k"
    return str(value)
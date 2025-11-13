# validators/post_validator.py


# 제목과 내용이 비어있는지 검사
def validate_not_empty(value: str) -> str:
    if not value or value.strip() == "":
        raise ValueError("title_and_content_required")
    return value

# 제목 길이 제한
def validate_title_length(value: str) -> str:
    if len(value.strip()) >= 26:
        raise ValueError("title_too_long")
    return value
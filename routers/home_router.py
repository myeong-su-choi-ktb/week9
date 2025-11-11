# routers/home_router.py
from fastapi import APIRouter
from controllers.home_controller import get_home_message

router = APIRouter()

@router.get("/")
def home():
    return get_home_message()
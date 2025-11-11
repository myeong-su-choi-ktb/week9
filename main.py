# main.py
from fastapi import FastAPI
from routers.home_router import router as home_router


app = FastAPI(title="Community Backend")

app.include_router(home_router)
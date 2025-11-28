import uvicorn
from fastapi import FastAPI

from src.app.api.movies import router as movies_router

app = FastAPI(
    title="Movies API",
    description="REST API for managing movie information",
    version="1.0.0"
)

app.include_router(movies_router)
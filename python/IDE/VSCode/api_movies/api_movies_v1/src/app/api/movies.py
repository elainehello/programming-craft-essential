from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session
from typing import List

from ..db.database import get_session
from ..models.movie import Movie, MovieCreate, MovieRead, MovieUpdate
from ..services.movie_service import MovieService

router = APIRouter(prefix="/api/v1/movies", tags=["movies-v1"])

def get_movie_service(session: Session = Depends(get_session)) -> MovieService:
    return MovieService(session)

@router.post("/", response_model=MovieRead)
def create_movie_v1(
    movie: MovieCreate,
    movie_service: MovieService = Depends(get_movie_service)
):
    try:
        return movie_service.create_movie(movie)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e)) from e
    

from typing import Optional
from sqlmodel import SQLModel, Field

class MovieBase(SQLModel):
    series_title: str = Field(index=True)
    released_year: Optional[int] = None
    certificate: Optional[str] = None
    runtime: Optional[str] = None
    genre: Optional[str] = Field(index=True)
    imdb_rating: Optional[float] = None
    overview: Optional[str] = None
    director: Optional[str] = None
    star1: Optional[str] = None
    star2: Optional[str] = None
    star3: Optional[str] = None
    star4: Optional[str] = None
    no_of_votes: Optional[int] = None
    gross: Optional[str] = None

class Movie(MovieBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

class MovieCreate(MovieBase):
    pass

class MovieRead(MovieBase):
    id: int

class MovieUpdate(SQLModel):
    series_title: Optional[str] = None
    released_year: Optional[int] = None
    certificate: Optional[str] = None
    runtime: Optional[str] = None
    genre: Optional[str] = None
    imdb_rating: Optional[float] = None
    overview: Optional[str] = None
    director: Optional[str] = None
    star1: Optional[str] = None
    star2: Optional[str] = None
    star3: Optional[str] = None
    star4: Optional[str] = None
    no_of_votes: Optional[int] = None
    gross: Optional[str] = None

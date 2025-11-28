from typing import List, Optional
from sqlmodel import Session
from ..models.movie import Movie, MovieCreate, MovieUpdate
from ..repositories.movie_repository import MovieRepository

class MovieService:
    """Service layer for movie business logic and validation."""
    
    def __init__(self, session: Session) -> None:
        self.repository = MovieRepository(session)

    def create_movie(self, movie_data: MovieCreate) -> Movie:
        """Create a new movie with business logic validation."""
        # Business logic validation
        self._validate_movie_data(movie_data)
        
        # Check if movie already exists
        if self.repository.movie_exists_by_title_and_year(
            movie_data.series_title, movie_data.released_year
        ):
            raise ValueError(
                f"Movie '{movie_data.series_title}' ({movie_data.released_year}) already exists"
            )
        
        return self.repository.create_movie(movie_data)

    def get_movie_by_id(self, movie_id: int) -> Optional[Movie]:
        """Get movie by ID with validation."""
        if movie_id <= 0:
            raise ValueError("Movie ID must be a positive integer")
        
        return self.repository.get_movie_by_id(movie_id)

    def get_all_movies(self, offset: int = 0, limit: int = 10) -> List[Movie]:
        """Get paginated list of movies with validation."""
        self._validate_pagination(offset, limit)
        return self.repository.get_all_movies(offset=offset, limit=limit)

    def update_movie(self, movie_id: int, movie_update: MovieUpdate) -> Optional[Movie]:
        """Update movie with business logic validation."""
        if movie_id <= 0:
            raise ValueError("Movie ID must be a positive integer")
        
        # Check if movie exists
        existing_movie = self.repository.get_movie_by_id(movie_id)
        if not existing_movie:
            return None
        
        # Validate update data
        self._validate_movie_update_data(movie_update)
        
        return self.repository.update_movie(movie_id, movie_update)

    def delete_movie(self, movie_id: int) -> bool:
        """Delete movie with validation."""
        if movie_id <= 0:
            raise ValueError("Movie ID must be a positive integer")
        
        return self.repository.delete_movie(movie_id)

    def search_movies(self, query: str, offset: int = 0, limit: int = 10) -> List[Movie]:
        """Search movies with validation."""
        if not query or len(query.strip()) < 2:
            raise ValueError("Search query must be at least 2 characters long")
        
        self._validate_pagination(offset, limit)
        return self.repository.search_movies(query.strip(), offset, limit)

    def get_movies_by_genre(self, genre: str, offset: int = 0, limit: int = 10) -> List[Movie]:
        """Get movies by genre with validation."""
        if not genre or len(genre.strip()) < 2:
            raise ValueError("Genre must be at least 2 characters long")
        
        self._validate_pagination(offset, limit)
        return self.repository.get_movies_by_genre(genre.strip(), offset, limit)

    def get_movies_by_year(self, year: int, offset: int = 0, limit: int = 10) -> List[Movie]:
        """Get movies by year with validation."""
        if year < 1888 or year > 2030:  # Cinema history bounds
            raise ValueError("Year must be between 1888 and 2030")
        
        self._validate_pagination(offset, limit)
        return self.repository.get_movies_by_year(year, offset, limit)

    def get_movies_by_director(self, director: str, offset: int = 0, limit: int = 10) -> List[Movie]:
        """Get movies by director with validation."""
        if not director or len(director.strip()) < 2:
            raise ValueError("Director name must be at least 2 characters long")
        
        self._validate_pagination(offset, limit)
        return self.repository.get_movies_by_director(director.strip(), offset, limit)

    def get_movies_by_rating_range(
        self, 
        min_rating: float, 
        max_rating: float, 
        offset: int = 0, 
        limit: int = 10
    ) -> List[Movie]:
        """Get movies by rating range with validation."""
        if min_rating < 0 or max_rating > 10:
            raise ValueError("Ratings must be between 0 and 10")
        
        if min_rating > max_rating:
            raise ValueError("Minimum rating cannot be greater than maximum rating")
        
        self._validate_pagination(offset, limit)
        return self.repository.get_movies_by_rating_range(min_rating, max_rating, offset, limit)

    def get_top_rated_movies(self, limit: int = 10) -> List[Movie]:
        """Get top rated movies with validation."""
        if limit <= 0 or limit > 100:
            raise ValueError("Limit must be between 1 and 100")
        
        return self.repository.get_top_rated_movies(limit)

    def get_movies_count(self) -> int:
        """Get total count of movies."""
        return self.repository.get_movies_count()

    def get_movies_by_multiple_filters(
        self,
        genre: Optional[str] = None,
        year: Optional[int] = None,
        min_rating: Optional[float] = None,
        director: Optional[str] = None,
        offset: int = 0,
        limit: int = 10
    ) -> List[Movie]:
        """Get movies with multiple filters and validation."""
        # Validate individual filters
        if genre and len(genre.strip()) < 2:
            raise ValueError("Genre must be at least 2 characters long")
        
        if year and (year < 1888 or year > 2030):
            raise ValueError("Year must be between 1888 and 2030")
        
        if min_rating and (min_rating < 0 or min_rating > 10):
            raise ValueError("Rating must be between 0 and 10")
        
        if director and len(director.strip()) < 2:
            raise ValueError("Director name must be at least 2 characters long")
        
        self._validate_pagination(offset, limit)
        
        return self.repository.get_movies_by_multiple_filters(
            genre=genre.strip() if genre else None,
            year=year,
            min_rating=min_rating,
            director=director.strip() if director else None,
            offset=offset,
            limit=limit
        )

    def get_recent_movies(self, years_back: int = 5, limit: int = 10) -> List[Movie]:
        """Get recent movies with validation."""
        if years_back <= 0 or years_back > 50:
            raise ValueError("Years back must be between 1 and 50")
        
        if limit <= 0 or limit > 100:
            raise ValueError("Limit must be between 1 and 100")
        
        return self.repository.get_recent_movies(years_back, limit)

    def bulk_create_movies(self, movies_data: List[MovieCreate]) -> List[Movie]:
        """Create multiple movies with validation."""
        if not movies_data:
            raise ValueError("Movies data list cannot be empty")
        
        if len(movies_data) > 100:
            raise ValueError("Cannot create more than 100 movies at once")
        
        # Validate each movie
        for i, movie_data in enumerate(movies_data):
            try:
                self._validate_movie_data(movie_data)
            except ValueError as e:
                raise ValueError(f"Invalid data for movie at index {i}: {str(e)}")
        
        # Check for duplicates within the batch
        titles_years = []
        for movie_data in movies_data:
            title_year = (movie_data.series_title, movie_data.released_year)
            if title_year in titles_years:
                raise ValueError(f"Duplicate movie in batch: '{movie_data.series_title}' ({movie_data.released_year})")
            titles_years.append(title_year)
        
        return self.repository.bulk_create_movies(movies_data)

    def get_movie_statistics(self) -> dict:
        """Get comprehensive movie statistics."""
        total_count = self.get_movies_count()
        top_movies = self.get_top_rated_movies(limit=5)
        recent_movies = self.get_recent_movies(years_back=1, limit=5)
        
        return {
            "total_movies": total_count,
            "top_rated_movies": [
                {
                    "title": movie.series_title,
                    "rating": movie.imdb_rating,
                    "year": movie.released_year
                } for movie in top_movies
            ],
            "recent_movies": [
                {
                    "title": movie.series_title,
                    "year": movie.released_year
                } for movie in recent_movies
            ]
        }

    # Private validation methods
    def _validate_movie_data(self, movie_data: MovieCreate) -> None:
        """Validate movie creation data."""
        if not movie_data.series_title or len(movie_data.series_title.strip()) < 1:
            raise ValueError("Movie title is required and cannot be empty")
        
        if movie_data.released_year and (movie_data.released_year < 1888 or movie_data.released_year > 2030):
            raise ValueError("Release year must be between 1888 and 2030")
        
        if movie_data.imdb_rating and (movie_data.imdb_rating < 0 or movie_data.imdb_rating > 10):
            raise ValueError("IMDB rating must be between 0 and 10")
        
        if movie_data.meta_score and (movie_data.meta_score < 0 or movie_data.meta_score > 100):
            raise ValueError("Meta score must be between 0 and 100")

    def _validate_movie_update_data(self, movie_update: MovieUpdate) -> None:
        """Validate movie update data."""
        if movie_update.series_title is not None and len(movie_update.series_title.strip()) < 1:
            raise ValueError("Movie title cannot be empty")
        
        if movie_update.released_year and (movie_update.released_year < 1888 or movie_update.released_year > 2030):
            raise ValueError("Release year must be between 1888 and 2030")
        
        if movie_update.imdb_rating and (movie_update.imdb_rating < 0 or movie_update.imdb_rating > 10):
            raise ValueError("IMDB rating must be between 0 and 10")
        
        if movie_update.meta_score and (movie_update.meta_score < 0 or movie_update.meta_score > 100):
            raise ValueError("Meta score must be between 0 and 100")

    def _validate_pagination(self, offset: int, limit: int) -> None:
        """Validate pagination parameters."""
        if offset < 0:
            raise ValueError("Offset must be non-negative")
        
        if limit <= 0 or limit > 1000:
            raise ValueError("Limit must be between 1 and 1000")
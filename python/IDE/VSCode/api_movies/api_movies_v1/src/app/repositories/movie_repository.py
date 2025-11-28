from typing import List, Optional
from sqlmodel import Session, select, and_, or_
from ..models.movie import Movie, MovieCreate, MovieUpdate

class MovieRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def create_movie(self, movie_data: MovieCreate) -> Movie:
        """Create a new movie record."""
        movie_dict = movie_data.model_dump()
        db_movie = Movie(**movie_dict)
        self.session.add(db_movie)
        self.session.commit()
        self.session.refresh(db_movie)
        return db_movie

    def get_movie_by_id(self, movie_id: int) -> Optional[Movie]:
        """Get a movie by its ID."""
        return self.session.get(Movie, movie_id)
   
    def get_all_movies(self, offset: int = 0, limit: int = 10) -> List[Movie]:
        """Get all movies with pagination."""
        result = self.session.exec(
            select(Movie).offset(offset).limit(limit)
        )
        return list(result.all())

    def update_movie(self, movie_id: int, movie_update: MovieUpdate) -> Optional[Movie]:
        """Update an existing movie."""
        db_movie = self.get_movie_by_id(movie_id)
        if not db_movie:
            return None
        
        update_data = movie_update.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_movie, field, value)

        self.session.commit()
        self.session.refresh(db_movie)
        return db_movie

    def delete_movie(self, movie_id: int) -> bool:
        """Delete a movie by ID."""
        db_movie = self.get_movie_by_id(movie_id)
        if not db_movie:
            return False
        
        self.session.delete(db_movie)
        self.session.commit()
        return True

    def search_movies(self, query: str, offset: int = 0, limit: int = 10) -> List[Movie]:
        """Search movies by title or overview."""
        result = self.session.exec(
            select(Movie).where(
                or_(
                    Movie.series_title.ilike(f"%{query}%"),
                    Movie.overview.ilike(f"%{query}%")
                )
            ).offset(offset).limit(limit)
        )
        return list(result.all())

    def get_movies_by_genre(self, genre: str, offset: int = 0, limit: int = 10) -> List[Movie]:
        """Get movies filtered by genre."""
        result = self.session.exec(
            select(Movie).where(Movie.genre.ilike(f"%{genre}%"))
            .offset(offset).limit(limit)
        )
        return list(result.all())

    def get_movies_by_year(self, year: int, offset: int = 0, limit: int = 10) -> List[Movie]:
        """Get movies filtered by release year."""
        result = self.session.exec(
            select(Movie).where(Movie.released_year == year)
            .offset(offset).limit(limit)
        )
        return list(result.all())

    def get_movies_by_director(self, director: str, offset: int = 0, limit: int = 10) -> List[Movie]:
        """Get movies filtered by director."""
        result = self.session.exec(
            select(Movie).where(Movie.director.ilike(f"%{director}%"))
            .offset(offset).limit(limit)
        )
        return list(result.all())

    def get_movies_by_rating_range(self, min_rating: float, max_rating: float, offset: int = 0, limit: int = 10) -> List[Movie]:
        """Get movies within a specific IMDB rating range."""
        result = self.session.exec(
            select(Movie).where(
                and_(
                    Movie.imdb_rating >= min_rating,
                    Movie.imdb_rating <= max_rating
                )
            ).offset(offset).limit(limit)
        )
        return list(result.all())

    def get_top_rated_movies(self, limit: int = 10) -> List[Movie]:
        """Get top rated movies."""
        result = self.session.exec(
            select(Movie).where(Movie.imdb_rating.is_not(None))
            .order_by(Movie.imdb_rating.desc())
            .limit(limit)
        )
        return list(result.all())

    def get_movies_count(self) -> int:
        """Get total count of movies."""
        result = self.session.exec(select(Movie))
        return len(list(result.all()))

    def movie_exists_by_title_and_year(self, title: str, year: Optional[int] = None) -> bool:
        """Check if a movie exists by title and optionally year."""
        query = select(Movie).where(Movie.series_title.ilike(f"%{title}%"))
        if year:
            query = query.where(Movie.released_year == year)
        
        result = self.session.exec(query)
        return result.first() is not None

    def get_movies_by_multiple_filters(
        self, 
        genre: Optional[str] = None,
        year: Optional[int] = None,
        min_rating: Optional[float] = None,
        director: Optional[str] = None,
        offset: int = 0,
        limit: int = 10
    ) -> List[Movie]:
        """Get movies with multiple filters applied."""
        query = select(Movie)
        
        conditions = []
        if genre:
            conditions.append(Movie.genre.ilike(f"%{genre}%"))
        if year:
            conditions.append(Movie.released_year == year)
        if min_rating:
            conditions.append(Movie.imdb_rating >= min_rating)
        if director:
            conditions.append(Movie.director.ilike(f"%{director}%"))
        
        if conditions:
            query = query.where(and_(*conditions))
        
        query = query.offset(offset).limit(limit)
        result = self.session.exec(query)
        return list(result.all())

    def get_recent_movies(self, years_back: int = 5, limit: int = 10) -> List[Movie]:
        """Get recent movies from the last N years."""
        from datetime import datetime
        current_year = datetime.now().year
        min_year = current_year - years_back
        
        result = self.session.exec(
            select(Movie).where(Movie.released_year >= min_year)
            .order_by(Movie.released_year.desc())
            .limit(limit)
        )
        return list(result.all())

    def bulk_create_movies(self, movies_data: List[MovieCreate]) -> List[Movie]:
        """Create multiple movies in bulk."""
        db_movies = []
        for movie_data in movies_data:
            movie_dict = movie_data.model_dump()
            db_movie = Movie(**movie_dict)
            self.session.add(db_movie)
            db_movies.append(db_movie)
        
        self.session.commit()
        for db_movie in db_movies:
            self.session.refresh(db_movie)
        
        return db_movies


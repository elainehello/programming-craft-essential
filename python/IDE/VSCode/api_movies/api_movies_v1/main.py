"""
Main application file for the Movies API.
Demonstrates proper SQLAlchemy setup with Docker Compose PostgreSQL.
"""
import uvicorn
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional

# Import our database configuration
from src.app.db.database import get_db, create_tables, test_connection
from src.app.models.movie import Movie

# Create FastAPI app
app = FastAPI(
    title="Movies API",
    description="A REST API for managing movie information with PostgreSQL backend",
    version="1.0.0"
)

# Create tables on startup
@app.on_event("startup")
async def startup_event():
    """
    Called when the application starts.
    Creates database tables and tests connection.
    """
    print("🚀 Starting Movies API...")
    
    # Test database connection
    if test_connection():
        print("✅ Database connection successful")
    else:
        print("❌ Database connection failed")
        return
    
    # Create tables
    try:
        create_tables()
        print("✅ Database tables created/verified")
    except Exception as e:
        print(f"❌ Error creating tables: {e}")

# Health check endpoint
@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "database": "connected" if test_connection() else "disconnected"
    }

# Example endpoints (you can expand these)
@app.get("/movies", response_model=List[dict])
async def get_movies(
    skip: int = 0, 
    limit: int = 10,
    db: Session = Depends(get_db)
):
    """Get list of movies"""
    movies = db.query(Movie).offset(skip).limit(limit).all()
    return [
        {
            "id": movie.id,
            "title": movie.series_title,
            "year": movie.released_year,
            "rating": float(movie.imdb_rating) if movie.imdb_rating else None,
            "genre": movie.genre
        } for movie in movies
    ]

@app.get("/movies/{movie_id}")
async def get_movie(movie_id: int, db: Session = Depends(get_db)):
    """Get a specific movie by ID"""
    movie = db.query(Movie).filter(Movie.id == movie_id).first()
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    
    return {
        "id": movie.id,
        "title": movie.series_title,
        "year": movie.released_year,
        "certificate": movie.certificate,
        "runtime": movie.runtime,
        "genre": movie.genre,
        "imdb_rating": float(movie.imdb_rating) if movie.imdb_rating else None,
        "overview": movie.overview,
        "director": movie.director,
        "stars": [movie.star1, movie.star2, movie.star3, movie.star4],
        "votes": movie.no_of_votes,
        "gross": movie.gross
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

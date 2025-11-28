from sqlalchemy import Column, Integer, String, Text, Numeric, BigInteger
from sqlalchemy.ext.declarative import declarative_base

BaseModel = declarative_base()

class Movie(BaseModel):
    __tablename__ = "movies"
    
    id = Column(Integer, primary_key=True, index=True)
    poster_link = Column(Text, nullable=True)
    series_title = Column(String, nullable=False, index=True)
    released_year = Column(Integer, nullable=True)
    certificate = Column(String(20), nullable=True)
    runtime = Column(String(50), nullable=True)
    genre = Column(Text, nullable=True)
    imdb_rating = Column(Numeric(3,1), nullable=True)
    overview = Column(Text, nullable=True)
    meta_score = Column(Integer, nullable=True)
    director = Column(Text, nullable=True)
    star1 = Column(Text, nullable=True)
    star2 = Column(Text, nullable=True)
    star3 = Column(Text, nullable=True)
    star4 = Column(Text, nullable=True)
    no_of_votes = Column(BigInteger, nullable=True)
    gross = Column(BigInteger, nullable=True)

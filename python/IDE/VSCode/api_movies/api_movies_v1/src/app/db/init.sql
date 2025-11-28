CREATE TABLE IF NOT EXISTS movies (
    id SERIAL PRIMARY KEY,
    poster_link TEXT,
    series_title TEXT NOT NULL,
    released_year INTEGER,
    certificate VARCHAR(20),
    runtime VARCHAR(50),
    genre TEXT,
    imdb_rating NUMERIC(3,1),
    overview TEXT,
    meta_score INTEGER,
    director TEXT,
    star1 TEXT,
    star2 TEXT,
    star3 TEXT,
    star4 TEXT,
    no_of_votes BIGINT,
    gross BIGINT
);
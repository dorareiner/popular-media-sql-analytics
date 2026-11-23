CREATE TABLE media_types (
    type_id SERIAL PRIMARY KEY,
    type_name VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE media_items (
    item_id SERIAL PRIMARY KEY,
    tmdb_id INT UNIQUE NOT NULL,
    title VARCHAR(255) NOT NULL,
    type_id INT REFERENCES media_types(type_id),
    search_category VARCHAR(100),
    original_language VARCHAR(20),
    genres VARCHAR(255),
    origin_country VARCHAR(100),
    release_date DATE,
    release_year INT,
    is_recent BOOLEAN,
    popularity NUMERIC(12, 4),
    vote_average NUMERIC(3, 1),
    vote_count INT,
    overview TEXT
);

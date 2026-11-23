# Popular Media SQL Analytics (Python & PostgreSQL)

End-to-end ETL data pipeline and SQL analytics project exploring popular movies and TV shows from TMDB (2026 dataset).

## Tech Stack
* **Python** (`pandas`, `psycopg`, `python-dotenv`, `kagglehub`)
* **PostgreSQL** (Relational database design, normalization, analytical SQL queries)

## Project Structure
* `download.py` – Downloads the dataset via KaggleHub API.
* `schema.sql` – Defines normalized PostgreSQL tables (`media_types`, `media_items`).
* `etl.py` – Cleans raw CSV data and loads records into PostgreSQL.
* `queries.sql` – Business and analytical SQL queries using `JOIN`, `GROUP BY`, and aggregations.

## How to Run
1. Create a PostgreSQL database named `popular_media_db` and run `schema.sql`.
2. Copy `.env.example` to `.env` and fill in your database credentials.
3. Install dependencies: `pip install -r requirements.txt`
4. Run `python download.py` and place the CSV into the `data/` folder.
5. Run `python etl.py` to populate the database.

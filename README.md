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

## Key Insights
Based on the SQL analysis of the 2026 TMDB dataset:

| Media Type | Total Titles | Average Rating | Average Popularity |
| :--- | :---: | :---: | :---: |
| **Movie** | `466` | `7.06` | `44.09` |
| **TV Show** | `522` | `7.57` | `71.55` |

* **Rating Trends:** TV shows maintain a higher average viewer rating (`7.57` vs. `7.06`) and higher average popularity compared to movies.
* **Top Performers:** The highest-rated title with over 500 votes is the TV show *Teach You a Lesson*.
* **Language Dominance:** English-language productions account for the vast majority of popular releases in the catalog.


import os
import csv
import pandas as pd
import psycopg
from dotenv import load_dotenv

load_dotenv()


def run_etl(csv_path):
    # 1. Extract: CSV beolvasása a beépített csv modullal
    with open(csv_path, mode='r', encoding='utf-8', errors='replace') as f:
        reader = csv.DictReader(f)
        # Oszlopnevek megtisztítása a felesleges szóközöktől
        cleaned_rows = []
        for row in reader:
            cleaned_rows.append({k.strip(): v for k, v in row.items() if k is not None})
        df = pd.DataFrame(cleaned_rows)

    print("Beolvasott oszlopok:", list(df.columns))

    # 2. Transform: Üres szövegek cseréje None-ra és évszám kezelése
    df = df.replace(r'^\s*$', None, regex=True)
    df = df.where(pd.notnull(df), None)

    conn_info = (
        f"dbname={os.getenv('DB_NAME')} user={os.getenv('DB_USER')} "
        f"password={os.getenv('DB_PASSWORD')} host={os.getenv('DB_HOST')} "
        f"port={os.getenv('DB_PORT', 5432)}"
    )

    # 3. Load: Adatok feltöltése PostgreSQL-be
    inserted_count = 0
    with psycopg.connect(conn_info) as conn:
        with conn.cursor() as cur:
            for _, row in df.iterrows():
                # Ha nincs id vagy cím, átugorjuk a hibás sort
                if not row.get('id') or not row.get('title'):
                    continue

                # Médiatípus beszúrása vagy lekérése
                m_type = row.get('media_type') or 'unknown'
                cur.execute(
                    """INSERT INTO media_types (type_name) VALUES (%s)
                       ON CONFLICT (type_name) DO UPDATE SET type_name = EXCLUDED.type_name
                       RETURNING type_id;""",
                    (m_type,)
                )
                type_id = cur.fetchone()[0]

                # Évszám kinyerése biztonságosan
                raw_year = row.get('release_year')
                release_year = None
                if raw_year:
                    try:
                        release_year = int(float(raw_year))
                    except ValueError:
                        release_year = None
                elif row.get('release_date') and len(str(row.get('release_date'))) >= 4:
                    try:
                        release_year = int(str(row.get('release_date'))[:4])
                    except ValueError:
                        release_year = None

                # Dátum ellenőrzése (csak érvényes YYYY-MM-DD formátumot engedünk át)
                r_date = row.get('release_date')
                if r_date and len(str(r_date)) != 10:
                    r_date = None

                # Számok biztonságos átalakítása
                try:
                    tmdb_id = int(float(row['id']))
                    popularity = float(row['popularity']) if row.get('popularity') else None
                    vote_avg = float(row['vote_average']) if row.get('vote_average') else None
                    vote_cnt = int(float(row['vote_count'])) if row.get('vote_count') else 0
                except (ValueError, TypeError):
                    continue

                cur.execute(
                    """INSERT INTO media_items (
                        tmdb_id, title, type_id, search_category, original_language,
                        genres, origin_country, release_date, release_year, is_recent,
                        popularity, vote_average, vote_count, overview
                    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    ON CONFLICT (tmdb_id) DO NOTHING;""",
                    (
                        tmdb_id,
                        row.get('title'),
                        type_id,
                        row.get('search_category'),
                        row.get('original_language'),
                        row.get('genres'),
                        row.get('origin_country'),
                        r_date,
                        release_year,
                        row.get('is_recent'),
                        popularity,
                        vote_avg,
                        vote_cnt,
                        row.get('overview')
                    )
                )
                inserted_count += 1
        conn.commit()
    print(f"Siker! Betoltve {inserted_count} film es sorozat a PostgreSQL adatbazisba.")


if __name__ == "__main__":
    run_etl("data/streaming_content_trends.csv")

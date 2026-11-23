-- 1. Filmek és sorozatok összehasonlítása (darabszám, átlagos értékelés, népszerűség)
SELECT
    t.type_name AS media_type,
    COUNT(i.item_id) AS total_count,
    ROUND(AVG(i.vote_average), 2) AS avg_rating,
    ROUND(AVG(i.popularity), 2) AS avg_popularity
FROM media_items i
JOIN media_types t ON i.type_id = t.type_id
GROUP BY t.type_name;

-- 2. Top 10 legmagasabbra értékelt produkció (legalább 500 szavazattal)
SELECT
    i.title,
    t.type_name,
    i.release_year,
    i.genres,
    i.vote_average,
    i.vote_count
FROM media_items i
JOIN media_types t ON i.type_id = t.type_id
WHERE i.vote_count >= 500
ORDER BY i.vote_average DESC, i.vote_count DESC
LIMIT 10;

-- 3. Legnépszerűbb eredeti nyelvek és átlagos értékelésük
SELECT
    original_language,
    COUNT(*) AS title_count,
    ROUND(AVG(vote_average), 2) AS avg_rating
FROM media_items
WHERE original_language IS NOT NULL
GROUP BY original_language
HAVING COUNT(*) >= 5
ORDER BY title_count DESC;

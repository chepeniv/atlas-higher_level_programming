-- sql script that list all records from two tables matching condition

-- list all shows withou a genre
SELECT title, genre_id
FROM tv_shows LEFT JOIN tv_show_genres
ON id = show_id
WHERE genre_id IS NULL;


-- sql script that list all genres and the number of shows in each

-- list genres and number of shows in each
SELECT name AS genre, COUNT(name) AS number_of_shows
FROM tv_genres LEFT JOIN tv_show_genres
ON id = genre_id
GROUP BY name
ORDER BY number_of_shows DESC;


-- sql script that list all records from one table matching condition

-- list matching records
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows 
LEFT OUTER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;

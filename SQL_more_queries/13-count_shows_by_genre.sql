--  lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
SELECT genres.name, COUNT(tv_shows.id) AS count
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY genres.name
HAVING COUNT(tv_shows_genres.show_id) > 0
ORDER BY count DESC;

--  lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
SELECT genres.name, COUNT(tv_shows.id) AS count
FROM genres
LEFT JOIN tv_show_genres
ON genres.id = tv_show_genres.genre_id
LEFT JOIN tv_shows
ON tv_show_genres.show_id = tv_shows.id
GROUP BY genres.name
ORDER BY count DESC, genres.name ASC;

# Write your MySQL query statement below
SELECT (
    SELECT name FROM Users
    INNER JOIN MovieRating ON MovieRating.user_id = Users.user_id
    GROUP BY MovieRating.user_id
    ORDER BY COUNT(*) DESC, name ASC
    LIMIT 1
) AS "results"
UNION ALL
SELECT (
    SELECT title FROM Movies
    INNER JOIN MovieRating ON MovieRating.movie_id = Movies.movie_id
    WHERE DATE_FORMAT(created_at, "%Y-%m") = "2020-02"
    GROUP BY MovieRating.movie_id
    ORDER BY AVG(rating) DESC, title ASC
    LIMIT 1
)
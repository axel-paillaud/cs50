SELECT movies.title FROM movies JOIN stars, people
ON stars.person_id = people.id AND stars.movie_id = movies.id
WHERE people.name = "Johnny Depp" INTERSECT
SELECT movies.title FROM movies JOIN stars, people
ON stars.person_id = people.id AND stars.movie_id = movies.id
WHERE people.name = "Helena Bonham Carter";
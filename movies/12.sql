SELECT movies.title FROM movies JOIN stars, people
ON stars.person_id = people.id AND stars.movie_id = movies.id
WHERE people.name = "Johnny Depp" AND people.name = "Helena Bonham Carter";

SELECT movies.title FROM movies JOIN stars, people ON stars.person_id = people.id AND stars.movie_id = movies.id IN (SELECT people.name = "Johnny Depp") AND (SELECT people.name = "Helena Bonham Carter");

SELECT movies.title FROM movies JOIN stars, people ON stars.person_id = people.id AND stars.movie_id = movies.id WHERE people.name = "Johnny Depp" AND people.name = "Helena Bonham Carter" IN people;

SELECT movies.title FROM movies JOIN stars, people ON stars.person_id = people.id AND stars.movie_id = movies.id WHERE people.name = "Johnny Depp";


SELECT movies.title FROM movies JOIN stars, people
ON stars.person_id = people.id AND stars.movie_id = movies.id
WHERE people.name = "Johnny Depp" INTERSECT
SELECT movies.title FROM movies JOIN stars, people
ON stars.person_id = people.id AND stars.movie_id = movies.id
WHERE people.name = "Helena Bonham Carter";
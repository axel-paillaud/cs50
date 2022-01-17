SELECT people.name from people JOIN stars, movies ON stars.person_id = people.id AND stars.movie_id = movies.id WHERE people.name = "Kevin Bacon";

SELECT people.name from people JOIN stars, movies ON stars.person_id = people.id AND stars.movie_id = movies.id WHERE EXISTS (SELECT movies.title from movies WHERE people.name = "Kevin Bacon" AND people.birth = 1958);

SELECT people.name from people JOIN stars, movies ON stars.person_id = people.id AND stars.movie_id = movies.id WHERE people.name = "Kevin Bacon";

SELECT people.name FROM people JOIN stars, movies ON stars.person_id = people.id AND stars.movie_id = movies.id WHERE people.name = (SELECT movies.title FROM movies JOIN stars, people ON stars.person_id = people.id AND stars.movie_id = movies.id WHERE people.name = "Kevin Bacon");

SELECT name FROM people WHERE id IN (SELECT person_id FROM stars WHERE movie_ID )

SELECT * FROM movies JOIN stars, people ON stars.person_id = people.id AND stars.movie_id = movies.id WHERE people.name = "Kevin Bacon";

SELECT movies.id FROM movies JOIN stars, people ON stars.person_id = people.id AND stars.movie_id = movies.id WHERE people.name = "Kevin Bacon";

SELECT people.name FROM people JOIN stars, movies ON stars.person_id = people.id AND stars.movie_ID = movies.id WHERE
movies.id = (SELECT movies.id FROM movies JOIN stars, people ON stars.person_id = people.id AND stars.movie_id = movies.id WHERE people.name = "Kevin Bacon");

SELECT people.name FROM people  WHERE movies.id = (SELECT movies.id FROM movies JOIN stars, people ON stars.person_id = people.id AND stars.movie_id = movies.id WHERE people.name = "Kevin Bacon");
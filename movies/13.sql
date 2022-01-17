SELECT people.name from people JOIN stars, movies ON stars.person_id = people.id AND stars.movie_id = movies.id WHERE people.name = "Kevin Bacon";

SELECT people.name from people JOIN stars, movies ON stars.person_id = people.id AND stars.movie_id = movies.id WHERE EXISTS (SELECT movies.title from movies WHERE people.name = "Kevin Bacon" AND people.birth = 1958);

SELECT people.name from people JOIN stars, movies ON stars.person_id = people.id AND stars.movie_id = movies.id WHERE people.name = "Kevin Bacon";

SELECT people.name FROM people JOIN stars, people ON stars.person_id = people.id AND stars.movie_id = movies.id WHERE (SELECT movies.title FROM movies JOIN stars, people ON stars.person_id = people.id AND stars.movie_id = movies.id WHERE people.name = "Kevin Bacon");
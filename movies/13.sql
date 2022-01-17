SELECT people.name from people JOIN stars, movies ON stars.person_id = people.id AND stars.movie_id = movies.id WHERE people.name = "Kevin Bacon";

SELECT people.name from people JOIN stars, movies ON stars.person_id = people.id AND stars.movie_id = movies.id WHERE EXISTS (SELECT people.name from people WHERE people.name = "Kevin Bacon" AND );
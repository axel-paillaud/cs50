SELECT people.name from people JOIN stars, movies ON stars.people_id = people.id AND stars.movie_id = movies.id WHERE people.name IN movies = "Kevin Bacon" AND people.birth = 1958;
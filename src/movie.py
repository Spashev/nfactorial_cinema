from .helpers import generate_id

from collections import namedtuple

Movie = namedtuple('Movie', ['id', 'name'])


class MovieFabrica:
    __movies = list()

    def addMovie(self, movie_name: str) -> Movie:
        movie = Movie(generate_id(), movie_name)
        self.__movies.append(movie)
        return movie

    def showAllMovies(self) -> None:
        print("# Вывод фильмов:")
        for movie in self.__movies:
            print(f"# {movie.id}. {movie.name.capitalize()}")

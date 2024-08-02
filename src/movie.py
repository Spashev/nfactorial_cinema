from .helpers import generate_id


class MovieFabrica:
    __movies = {}

    def addMovie(self, movie_name: str) -> str:
        movie_id = generate_id()
        self.__movies[movie_id] = movie_name
        return movie_id

    def showAllMovies(self) -> None:
        print("# Вывод фильмов:")
        for movie_id, movie_name in self.__movies.items():
            print(f"# {movie_id}. {movie_name.capitalize()}")

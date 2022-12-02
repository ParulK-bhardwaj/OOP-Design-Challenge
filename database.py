from movie import Movie;

class Database(Movie):
    def __init__(self):
        self.movie_list= []
        
    def _add_movie(self, movie):
        self.movie_list.append(movie)

    def _remove_movie(self, movie):
        self.movie_list.remove(movie)

    def __str__(self):
        out = ""

        for movie in self.movie_list:
            out += str(movie)

        return out

    def filter_by_genre(self, genre):
        pass
from movie import Movie;

class Database(Movie):
    def __init__(self):
        self.movie_list= []

    def add_movie(self, movie):
        self.movie_list.append(movie)

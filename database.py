from movie import Movie;

class Database(Movie):
    def __init__(self):
        self.__movie_list= []
    
    #public because it needs to be accessed outside of this class and subclasses
    def add_movie(self, movie):
        self.__movie_list.append(movie)
    #public because it needs to be accessed outside of this class and subclasses
    def remove_movie(self, movie):
        self.__movie_list.remove(movie)
    #cannot be used outside of class therefore is private
    def __str__(self):
        out = ""

        for movie in self.movie_list:
            out += str(movie)

        return out
        
    #public because it needs to be accessed outside of this class and subclasses
    def filter_by_genre(self, genre):

        filtered_movies = []

        for movie in self.__movie_list:
            if genre == movie.genre:
                filtered_movies.append(movie)

        return filtered_movies
from action import ActionMovie
from comedy import ComedyMovie
from scifi import SciFiMovie
import movie

class Database():
    def __init__(self):
        self.__movie_list = []
    
    #public because it needs to be accessed outside of this class and subclasses
    def add_movie(self, movie):
        self.__movie_list.append(movie)

    #public because it needs to be accessed outside of this class and subclasses
    def remove_movie(self, movie):
        self.__movie_list.remove(movie)



    def movie_list_display(self):
        number = 0
        for movie in self.__movie_list:
            number += 1
            print(f"Movie {number}")
            print(movie.__str__())
            print(movie.reason_to_watch())
            
    #public because it needs to be accessed outside of this class and subclasses
    # def filter_by_genre(self, genre):
    #     pass
    #     filtered_movies = [] 
    #     for movie in self.__movie_list:
    #         if genre.lower() == movie.genre.lower():
    #             filtered_movies.append(movie)
    #             print(filtered_movies)
    #     return filtered_movies.__str__()

if __name__ == "__main__":
    disney_database = Database()

    bad_guys = ComedyMovie("The BAD GUYS", 2022, "Pierre Perifel", ["Sam Rockwell", "Marc Maron"], "english")
    mad_max = ActionMovie("Mad Max: Fury Road", 2015, "George Miller", ["Charlize Theron", "Tom Hardy"], "english")
    star_wars = SciFiMovie("Star Wars: The Rise of Skywalker", 2019,"J.J. Abrams",["Carrie Fisher", "Mark Hamill", "Adam Driver", "Daisy Ridley", "John Boyega"], "english" )

    movies_entries = [bad_guys, mad_max, star_wars]
    for entry in movies_entries:
        disney_database.add_movie(entry)

    disney_database.movie_list_display()
    # print(disney_database.filter_by_genre("Comedy"))



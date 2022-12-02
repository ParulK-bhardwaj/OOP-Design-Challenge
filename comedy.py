from movie import Movie

class ComedyMovie(Movie):
    def __init__(self, title, year, genre, director, cast_members, language):
        super().__init__(title, year, genre, director, cast_members, language)
        

    def reason_to_watch(self):
        print(f"if you are fan of {self.genre} movies, you are in for a fun time.")
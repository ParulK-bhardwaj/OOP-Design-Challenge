from movie import Movie

class ComedyMovie(Movie):
    def __init__(self, title, year, director, cast_members, language):
        genre = 'Comedy'
        super().__init__(title, year, genre, director, cast_members, language)

    def reason_to_watch(self):
        return(f"if you are fan of {self.genre} movies, you are in for a fun time.")

if __name__ == "__main__":
    bad_guys = ComedyMovie("The BAD GUYS", 2022, "Pierre Perifel", ["Sam Rockwell", "Marc Maron"], "english")
    
    print(bad_guys.__str__())
    print(bad_guys.reason_to_watch())

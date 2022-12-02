from movie import Movie

class SciFiMovie(Movie):
    def __init__(self, title, year, genre, director, cast_members, language):
        super().__init__(title, year, genre, director, cast_members, language)
        

    def reason_to_watch(self):
        print(f"{self.genre} genre have stories involving conflicts between science and technology, human nature, and social organization in futuristic or fantastical settings")
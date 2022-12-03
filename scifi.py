from movie import Movie

class SciFiMovie(Movie):
    def __init__(self, title, year, director, cast_members, language):
        genre = 'Sci-fi'
        super().__init__(title, year, genre, director, cast_members, language)
        
    def reason_to_watch(self):
        return(f"{self.genre} genre have stories involving conflicts between science and technology, human nature, and social organization in futuristic or fantastical settings.")

if __name__ == "__main__":
    star_wars = SciFiMovie("Star Wars: The Rise of Skywalker", 2019,"J.J. Abrams",["Carrie Fisher", "Mark Hamill", "Adam Driver", "Daisy Ridley", "John Boyega"], "english" )
    
    print(star_wars.years_old(star_wars.year))
    print(star_wars.reason_to_watch())

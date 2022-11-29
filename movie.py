class Movie:
    def __init__(self, genre, title, director):
        self.genre = genre
        self.title = title
        self.director = director
        self.cast_members = []

    def __repr__(self):
        output = f"Title:{self.title}\nDirector:{self.director}\nGenre:{self.genre}\n"

        # for cast in self.cast_members:
        return output
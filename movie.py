class Movie:
    def __init__(self, title, year, genre, director, cast_members, language):
        self.title = title #string
        self.year = year #number
        self.genre = genre #string
        self.director = director #string
        self.cast_members = cast_members #list
        self.language = language #string

    def __str__(self):
        return f"""
        Title: {self.title}
        Year: {self.year}
        Genre: {self.genre}
        Director: {self.director}
        Cast: {', '.join(self.cast_members)}
        Language: {self.language}
        """

if __name__ == "__main__":
    pride = Movie('Pride and Prejudice', 2005, 'romantic-drama', 'Joe Wright', ['Keira Knightley', 'Matthew Macfadyen'], 'English',)
    print(pride.__str__())
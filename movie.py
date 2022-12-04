# impoted datetime to get the cuurent year
import datetime

class Movie:
    def __init__(self, title, year, genre, director, cast_members, language):
        self.title = title #string
        self.year = year #number
        self.genre = genre #string
        self.director = director #string
        self.cast_members = cast_members #list
        self.language = language #string

    #  The string method depends to the class and we wouldn't access it outside of this class.
    def __str__(self):
        return f"""
        Title: {self.title}
        Year: {self.year}
        Genre: {self.genre}
        Director: {self.director}
        Cast: {', '.join(self.cast_members)}
        Language: {self.language}
        """

    # We don't want subclasses of the class to change/override this method.
    @staticmethod
    def years_old(year):
        years = datetime.datetime.now().year - int(year)
        if years == 0:
            return(f"This movie is pretty recent. It just released this year")
        else:
            return(f"It has been {datetime.datetime.now().year - int(year)} years since the movie's release.")

if __name__ == "__main__":
    pride = Movie('Pride and Prejudice', 2005, 'romantic-drama', 'Joe Wright', ['Keira Knightley', 'Matthew Macfadyen'], 'English')
    print(pride.__str__())
    # Static methods in Python cannot access instance attributes so we have pulled it from the Movie class.
    print(pride.years_old(pride.year))
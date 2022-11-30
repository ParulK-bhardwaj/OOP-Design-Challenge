class Movie:
    def __init__(self, genre, title, director):
        self.genre = genre
        self.title = title
        self.director = director
        self.cast_members = []

    def __str__(self):
        output = f"Title:{self.title}\nDirector:{self.director}\nGenre:{self.genre}\n"

        # for cast in self.cast_members:
        return output

    def add_cast(self, name, role):
        """
        adds a dict object representing a cast member to cast_members list
        """

        member = {
            "name":name,
            "role":role
        }

        self.cast_members.append(member)

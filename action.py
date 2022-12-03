from movie import Movie

class ActionMovie(Movie):
    def __init__(self, title, year, director, cast_members, language):
        genre = 'Action'
        super().__init__(title, year, genre, director, cast_members, language)

    def reason_to_watch(self):
        return (f"if you are a fan of {self.genre} movies, you'll love all the action sequences here")

if __name__ == "__main__":
    mad_max = ActionMovie("Mad Max: Fury Road", 2015, "George Miller", ["Charlize Theron", "Tom Hardy"], "english")
    
    print(mad_max.__str__())
    print(f'{mad_max.reason_to_watch()} in this amazing movie called "{mad_max.title}".\n')
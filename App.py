from streamingService import StreamingService
from database import Database
from movie import Movie
from comedy import ComedyMovie
from action import ActionMovie

class App: 
  def __init__(self, name, description):
    self.streaming_services = {}
    self.name = name
    self.description = description
  
  # protected so that it can only be invoked from within the implementation of the app class
  def _add_streaming_service(self, streaming_service):
    self.streaming_services[streaming_service.name] = streaming_service

   # protected so that it can only be invoked from within the implementation of the app class
  def _remove_streaming_service(self, streaming_service):
    del self.streaming_services[streaming_service.name]

  def __str__(self): 
    description = f'Name: {self.name} description:{self.description}'
    return description

  def streaming_services_available(self):
    for service in self.streaming_services:
      print(service.title())

if __name__ == '__main__':
  movie_bundle = App("Movie Bundle", "At Movie Bundle, you can access movies from different streaming services all in one place.")
  disney_database = Database()
  abc_database = Database()

  space_balls = ComedyMovie("Space Balls", 1990, "idk", ["no clue"], "english")
  time_die = ActionMovie("No time to die", 1995, "who cares", ["loser1", "loser2"], "english")

  disney_plus = StreamingService("disney plus", "disney's streaming service", 10.99, 10, disney_database)
  abc = StreamingService("abc", "Abc's streaming service", 8.99, 10, abc_database)

  print(">>>>>>>Streaming Services Available>>>>>>>>>>")
  movie_bundle._add_streaming_service(disney_plus)
  movie_bundle._add_streaming_service(abc)
  movie_bundle.streaming_services_available()

  print("\n>>>>>>>ABC Streaming Service removed>>>>>>>>>>\n")
  movie_bundle._remove_streaming_service(abc)

  print("\n>>>>>>>Streaming Services Available>>>>>>>>>>")
  movie_bundle.streaming_services_available()

  movie_bundle.streaming_services["disney plus"].database.add_movie(space_balls)
  movie_bundle.streaming_services["disney plus"].database.add_movie(time_die)

  print("\n>>>>>>>Display movies from the database>>>>>>>>>>")
  movie_bundle.streaming_services["disney plus"].database.movie_list_display()

  print("\n>>>>>>>Display Comedy movies to pick from the database>>>>>>>>>>")
  movie_bundle.streaming_services["disney plus"].database.filter_by_genre("comedy")

  
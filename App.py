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
    #TODO instantiate

  
  def add_streaming_service(self, streaming_service):
    self.streaming_services[streaming_service.name] = streaming_service

  def remove_streaming_service(self, streaming_service): 
    self.streaming_services.remove(streaming_service.name)

  #TODO __str__() name and description
  def _str_(self): 
    description = f'Name: {self.name} description:{self.description}'

if __name__ == '__main__':
  app = App("app", "a test app")
  database = Database()

  comedy = ComedyMovie("Space Balls", 1990, "idk", ["no clue"], "english")
  action = ActionMovie("No time to die", 1995, "who cares", ["loser1", "loser2"], "english")

  s1 = StreamingService("disney plus", "disney's streaming service", 10.99, 10, database)

  app.add_streaming_service(s1)

  app.streaming_services["disney plus"].database.add_movie(action)
  app.streaming_services["disney plus"].database.add_movie(comedy)

  print(str(app.streaming_services["disney plus"]))

  
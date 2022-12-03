import itertools
from database import Database
from action import ActionMovie
from comedy import ComedyMovie
from scifi import SciFiMovie

class StreamingService(): 
  new_id = itertools.count()
  def __init__(self, name, description, subscription_fee, annual_discount, database):
    self.id = next(StreamingService.new_id)
    self.database = Database()
    self.name = name
    self.description = description
    self.subscription_fee = subscription_fee
    self.annual_discount = annual_discount #number -> in percent for e.g. 10

  def welcome(self): 
    message = f"Hey there! Welcome to {self.name}! We are glad you picked us. We offer unlimited entertainment with only ${self.subscription_fee} per month!"
    print(message)
  
  def add_streaming_service(self, streaming_service):
    self.streaming_services[streaming_service.id] = streaming_service
    
  def remove_streaming_service(self, streaming_service):
    self.streaming_services.pop(streaming_service.id)

  def pay_subscription(self, is_annual):
    if is_annual == True:
      discounted_fee = round(12 * self.subscription_fee * (1 - self.annual_discount/100), 2)
      charge = f"Your Annual subscription fee is ${discounted_fee}. You saved ${round((12 * self.subscription_fee) - discounted_fee, 2)}."
      print(charge)
    else:
      charge = f"Your Monthly subscription fee is {self.subscription_fee}."
      print(charge) 

  def movies_display(self):
    pass

if __name__ == "__main__":
  disney_database = Database()

  bad_guys = ComedyMovie("The BAD GUYS", 2022, "Pierre Perifel", ["Sam Rockwell", "Marc Maron"], "english")
  mad_max = ActionMovie("Mad Max: Fury Road", 2015, "George Miller", ["Charlize Theron", "Tom Hardy"], "english")
  star_wars = SciFiMovie("Star Wars: The Rise of Skywalker", 2019,"J.J. Abrams",["Carrie Fisher", "Mark Hamill", "Adam Driver", "Daisy Ridley", "John Boyega"], "english" )

  movies_entries = [bad_guys, mad_max, star_wars]
  for entry in movies_entries:
      disney_database.add_movie(entry)
  disney_plus = StreamingService("Disney+", "abc", 8.99, 10, disney_database)
  disney_plus.pay_subscription(True)
  disney_plus.welcome()
  print(disney_plus.movies_display())
  

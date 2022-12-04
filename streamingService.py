import itertools
from database import Database
from action import ActionMovie
from comedy import ComedyMovie
from scifi import SciFiMovie

class StreamingService(): 
  new_id = itertools.count()
  def __init__(self, name, description, subscription_fee, annual_discount, database):
    self.id = next(StreamingService.new_id)
    self.database = database
    self.name = name
    self.description = description  
    self.__subscription_fee = subscription_fee #private: So that it can't be changed outside of this class (We can put getter and setters to be able to access)
    self.__annual_discount = annual_discount #number; private: So that it can't be changed outside of this class

  def welcome(self): 
    message = f"Hey there! Welcome to {self.name}! We are glad you picked us. We offer unlimited entertainment with only ${self.__subscription_fee} per month!"
    print(message)

  def pay_subscription(self, is_annual):
    if is_annual == True:
      discounted_fee = round(12 * self.__subscription_fee * (1 - self.__annual_discount/100), 2)
      charge = f"Your Annual subscription fee is ${discounted_fee}. You saved ${round((12 * self.__subscription_fee) - discounted_fee, 2)}."
      print(charge)
    else:
      charge = f"Your Monthly subscription fee is {self.__subscription_fee}."
      print(charge) 

  def __str__(self):
    return f"name: {self.name} description:{self.description} cost:{self.__subscription_fee} Available Movies:{str(self.database)}"

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
  disney_database.movie_list_display()
  

import itertools
<<<<<<< HEAD
import database from database 
=======
from database import Database
>>>>>>> origin/main

class StreamingService: 
  new_id = itertools.count()
  def __init__(self, name, description, subscription_fee, movie_database):
    self.id = next(StreamingService.new_id)
    self.name = name 
    self.description = description 
    self.subscription_fee = subscription_fee 
    self.movie_database = movie_database

<<<<<<< HEAD
  def add_movie(self, movie): 
    self.movies._add_movie()

  def remove_movie(self, movie):
    self.movies._remove_movie()
=======
    print(self.id)

  #TODO __str__() print name fee, and description

  #TODO pay_subscription(is_annual) charge only do not check timing
>>>>>>> origin/main

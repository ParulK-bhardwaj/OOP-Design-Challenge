import itertools
from database import Database

class StreamingService: 
  new_id = itertools.count()
  def __init__(self, name, description, subscription_fee, movie_database):
    self.id = next(StreamingService.new_id)
    self.name = name 
    self.description = description 
    self.subscription_fee = subscription_fee 
    self.movie_database = movie_database

    print(self.id)

  #TODO __str__() print name fee, and description

  #TODO pay_subscription(is_annual) charge only do not check timing
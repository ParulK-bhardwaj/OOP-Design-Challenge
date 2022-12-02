import itertools
import database from database 

class StreamingService: 
  new_id = itertools.count()
  def __init__(self, name, description, subscription_fee):
    self.id = next(StreamingService.new_id)
    self.name = name 
    self.description = description 
    self.subscription_fee = subscription_fee 
    self.movies = {}

  def add_movie(self, movie): 
    self.movies._add_movie()

  def remove_movie(self, movie):
    self.movies._remove_movie() 
     print(self.id)

  #TODO __str__() print name fee, and description
  def _str_(self): 
    description = f'Hey there! Here is the subscription information. Name: {self.name}. Description: {self.description}. Subscription Fee: {self.subscription_fee} '
    print(description)

  #TODO pay_subscription(is_annual) charge only do not check timing
  def pay_subscription(is_annual): 
    if is_annual = True: 
      charge = 'You owe 50.99'
      print(charge)
    else: 
      charge = 'You owe 12.99'
      print(charge)

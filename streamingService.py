import itertools

class StreamingService: 
  new_id = itertools.count()
  def __init__(self, name, description, subscription_fee):
    self.id = next(StreamingService.new_id)
    self.name = name 
    self.description = description 
    self.subscription_fee = subscription_fee 
    self.movies = {}

  def add_movie(self, movie): 
    self.movies[movie.id] = movie

  def remove_movie(self, movie):
    self.movies.pop(movie.id)

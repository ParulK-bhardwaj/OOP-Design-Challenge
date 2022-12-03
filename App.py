from streamingService import StreamingService

class App: 
  def __init__(self, name, description):
    self.streaming_services = []
    self.name = name 
    self.description = description
    #TODO instantiate

  def add_streaming_service(self, streaming_service):
    self.streaming_services[streaming_service.id] = streaming_service

  def remove_streaming_service(self, streaming_service): 
    self.streaming_services.pop(streaming_service.id)

  #TODO __str__() name and description
  def _str_(self): 
    description = f'Hey there! Here is your streaming service information. Name: {self.name}. Description: {self.description}.'
    print(description)


if __name__ == '__main__':
  app = App("Movie Bundle", "abc")
  s1 = StreamingService("s1", "abc", 80)
  s2 = StreamingService("s2", "movie", 80)
  s3 = StreamingService("s3", "movie", 80)

  app.add_streaming_service(s1)
  app.add_streaming_service(s2)
  app.add_streaming_service(s3)
  print(app.streaming_services)

  app.remove_streaming_service(s2)
  print(app.streaming_services)

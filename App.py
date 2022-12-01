from StreamingService import StreamingService

class App: 
  def __init__(self):
    self.streaming_services = {}

  def add_streaming_service(self, streaming_service):
    self.streaming_services[streaming_service.id] = streaming_service

  def remove_streaming_service(self, streaming_service): 
    self.streaming_services.pop(streaming_service.id)

if __name__ == '__main__':
  # app = App()
  # s1 = StreamingService("s1", "movie", 80)
  # s2 = StreamingService("s2", "movie", 80)
  # s3 = StreamingService("s3", "movie", 80)

  # app.add_streaming_service(s1)
  # app.add_streaming_service(s2)
  # app.add_streaming_service(s3)
  # print(app.streaming_services)

  # app.remove_streaming_service(s2)
  # print(app.streaming_services)

import time

import ezsearch_pb2

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class Greeter(ezsearch_pb2.BetaGreeterServicer):
  global db
  db={}

  def Put(self, request, context):
    print "Server printing" , request.id , request.name

    db[request.id]=request.name
    return ezsearch_pb2.Response(message='Details added to server' )

  def Get(self,request,context):
    a=request.get_id
        
    if db.has_key(a):
      print "The is valid :)"
      return ezsearch_pb2.RespondDetails(get_id_result=a,name=db[a])
    else:
      print "Sorry, The key doesn't exist :( "
      return ezsearch_pb2.RespondDetails(get_id_result="0",name="0")


def serve():
  server = ezsearch_pb2.beta_create_Greeter_server(Greeter())
  server.add_insecure_port('[::]:50051')
  server.start()
  try:
    while True:
      time.sleep(_ONE_DAY_IN_SECONDS)
  except KeyboardInterrupt:
    server.stop(0)

if __name__ == '__main__':
  serve() 

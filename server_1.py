import time
import json
import os
import ezsearch_pb2

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class Greeter(ezsearch_pb2.BetaGreeterServicer):
  # global db
  db={}

  def Put(self, request, context):
    print "Server_1 printing" , request.id , request.name
    print('going to open json file')

    if (os.stat('50051.json').st_size<=0):
      json.dump(Greeter.db,open('50051.json','w'))

    db=json.load(open('50051.json','r'))
    print('json opened and going to print db')
    db[request.id]=request.name
    print db
    print('db printed and going to dump')
    json.dump(db,open('50051.json','w'))
    print('db dumped and sending response to client ')
    return ezsearch_pb2.Response(message='Details added to server' )

  def Get(self,request,context):
    a=request.get_id
    db=json.load(open('50051.json','r'))
    if db.has_key(a):
      print "The key is valid :)"
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

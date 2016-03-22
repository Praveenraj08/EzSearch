from grpc.beta import implementations
import sys
import helloworld_pb2

_TIMEOUT_SECONDS = 10


def f1(stub):
  search_id=raw_input("Please enter the ID to be searched :")
  response = stub.Get(helloworld_pb2.GetDetails(get_id=search_id), _TIMEOUT_SECONDS)
  #print response
  print "*******************Search Results are *************************** "
  print "Key   :" ,response.get_id_result
  print "Value :" ,response.name
  print "******************************************************************"
  ch=raw_input("Continue? y/n :")
  if ch=='y':
    run()
  else:
    sys.exit('Exiting client')
def run():
  channel = implementations.insecure_channel('localhost', 50051)
  stub = helloworld_pb2.beta_create_Greeter_stub(channel)
  ID=raw_input("Please enter your ID : ")
  fname=raw_input("Please enter your Name : ")


  response = stub.Put(helloworld_pb2.PutDetails(id=ID,name=fname), _TIMEOUT_SECONDS)
  print "printing message from server"
  print "Greeter client received: " + response.message

  f1(stub)
 

if __name__ == '__main__':
  run()

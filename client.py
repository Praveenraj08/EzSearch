from grpc.beta import implementations

import ezsearch_pb2

_TIMEOUT_SECONDS = 10

class client_module(object):
	def __init__(self,host,port):

		self.channel = implementations.insecure_channel(host,int(port))
		self.stub = ezsearch_pb2.beta_create_Greeter_stub(self.channel)

	def f1(self,getkey):

		search_id=getkey
		response =self.stub.Get(ezsearch_pb2.GetDetails(get_id=search_id), _TIMEOUT_SECONDS)

		print "*******************Search Results are *************************** "
		print "Key   :" ,response.get_id_result
		print "Value :" ,response.name
		print "******************************************************************"
					 
	def run(self,key,value):
		ID=key 
		fname=value

		response = self.stub.Put(ezsearch_pb2.PutDetails(id=ID,name=fname), _TIMEOUT_SECONDS)
		print "printing message from server"
		print "Greeter client received: " + response.message

from grpc.beta import implementations

import ezsearch_pb2
import socket

_TIMEOUT_SECONDS = 10

class client_module(object):
	def __init__(self,host,port):
		try :
			# socket.getaddrinfo(host,port)
			# socket.getservbyport(port)

			self.channel = implementations.insecure_channel(host,int(port))
			self.stub = ezsearch_pb2.beta_create_Greeter_stub(self.channel)
		except :
			print "Problem with the connection"

	def f1(self,getkey):

		search_id=getkey
		response =self.stub.Get(ezsearch_pb2.GetDetails(get_id=search_id), _TIMEOUT_SECONDS)
		if response.get_id_result !='0':
			print "*******************Search Results are *************************** "
			print "Key   :" ,response.get_id_result
			print "Value :" ,response.name
			print "******************************************************************"
		else:
			print "No key found"
					 
	def run(self,key,value):
		# print('back to run')
		ID=key 
		fname=value
		print('going tot send to values to server')
		response = self.stub.Put(ezsearch_pb2.PutDetails(id=ID,name=fname), _TIMEOUT_SECONDS)
		print('back to run method ')
		print "printing message from server"
		print "Greeter client received: " + response.message

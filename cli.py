import cmd
import string, sys
import os
from uhashring import HashRing
from client import client_module


class CLI(cmd.Cmd):
		global client_obj
		hr=HashRing(nodes=['50051','50052','50053'])

	
		list_connect = []
		list_put = []
		list_get = []


		# def preloop(self):
		# 		print "<<< connect --host localhost --port 50051 >>>"

		def postloop(self):
				print "Connection closed "

		# def do_connect(self, arg1):
		# 		print arg1
		# 		CLI.list_connect = arg1.split()
		# 		if len(CLI.list_connect) != 4:
		# 				print "Invalid Syntax"
		# 				cli.cmdloop()
		# 		if CLI.list_connect[0] != '--host':
		# 				print "Invalid Syntax"
		# 				cli.cmdloop()
		# 		if CLI.list_connect[2] != '--port':
		# 				print "Syntax error. << --port >>"
		# 				cli.cmdloop()
				
		# 		CLI.client_obj=client_module(CLI.list_connect[1], CLI.list_connect[3])
				
				



		def do_put(self, arg):
				CLI.list_put = arg.split()
				if(len(CLI.list_put)!=4):
						print "Invalid Syntax"
						cli.cmdloop()
				if CLI.list_put[0] != '--key':
						print "Syntax Error"
						cli.cmdloop()
				if CLI.list_put[2] != '--value':
						print "Syntax Error"
						cli.cmdloop()

				key=CLI.list_put[1]
				which_port=str(CLI.hr.get_node(key))
				print(which_port)
				host='localhost'
				CLI.client_obj=client_module(host,which_port)
				try:
					CLI.client_obj.run(CLI.list_put[1], CLI.list_put[3])
					print('sent to run method')
				except AttributeError:
					print "Sorry no connection to the server"
					cli.cmdloop()


		def do_get(self, arg):
				CLI.list_get = arg.split()
				if(len(CLI.list_get)!=2):
						print "Invalid Syntax"
						cli.cmdloop();
				if(CLI.list_get[0]!='--key'):
						print "Invalid Syntax"
						cli.cmdloop();
				key=CLI.list_get[1]
				which_port=CLI.hr.get_node(key)
				host='localhost'
				CLI.client_obj=client_module(host,which_port)
				try:
						CLI.client_obj.f1(CLI.list_get[1])
				except AttributeError:
						print "Sorry no connection to the server to get value"
						cli.cmdloop()


		def __init__(self):
				cmd.Cmd.__init__(self)
				self.prompt = '--> '

		
		def do_quit(self, arg):
				os.system('kill $(lsof -t -i:50051)')
				sys.exit(1)

		def do_disconnect(self, arg):

				try:
						del CLI.client_obj
						print "Disconnected from server"
				except:
						print "Sorry no connection to the server"
						cli.cmdloop()
				

		def help_quit(self):
				print "syntax: quit",
				print "-- terminates the application"
						
		def help_connect(self):
				print '''
				NAME  - connect

				SYNOPSIS - connect [--host] [host number] [--port] [port number]

				DESCRIPTION - Use the command to the specified host and port.

				OPTIONS - "connect" does not take any options.
										User has to supply the host and port number"

				'''


		def help_get(self):
				'''
				print NAME  - get

				SYNOPSIS - get [--key] [key value] 

				DESCRIPTION - Use the command to get value for the supplied key.

				OPTIONS - "get" does not take any options.
										User has to supply the key ot rerieve the value, if exists"

				'''

		def help_put(self):
				print '''                  
				NAME  - put

				SYNOPSIS - put [--key] [key] [--value] [value]

				DESCRIPTION - Use the command to the put the key and the value to the server.

				OPTIONS - "put" does not take any options.
									 User has to supply the key and the value"

				'''

		def help_disconnect(self):
				print '''
				NAME  - disconnect

				SYNOPSIS - diconnect

				DESCRIPTION - Use the command to disconnect from the host , if connection exists.

				OPTIONS - "disconnect" does not take any options.
									 

				'''

	 
cli = CLI()
cli.cmdloop()

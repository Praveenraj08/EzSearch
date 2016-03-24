import cmd
import string, sys
import os
from client import client_module


class CLI(cmd.Cmd):
    global client_obj
  
    list_connect = []
    list_put = []
    list_get = []


    def preloop(self):
        print "<<< connect --host localhost --port 50051 >>>"

    def postloop(self):
        print "Connection closed "

    def do_connect(self, arg1):
        print arg1
        CLI.list_connect = arg1.split()
        if len(CLI.list_connect) != 4:
            print "Invalid Syntax"
            cli.cmdloop()
        if CLI.list_connect[0] != '--host':
            print "Invalid Syntax"
            cli.cmdloop()
        if CLI.list_connect[2] != '--port':
            print "Syntax error. << --port >>"
            cli.cmdloop()
        
        CLI.client_obj=client_module(CLI.list_connect[1], CLI.list_connect[3])


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
        try:
            CLI.client_obj.run(CLI.list_put[1], CLI.list_put[3])
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



        try:
            CLI.client_obj.f1(CLI.list_get[1])
        except AttributeError:
            print "Sorry no connection to the server"
            cli.cmdloop()


    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = '--> '

    def help_connect(self):
        print '''                  <<keyword>> <<keyword>     <<IP>>    <<keyword>> <<Port number>>
				  <<connect>> <<--host>> <<localhost>>  <<--port>>    <<50051>>'''

    def do_quit(self, arg):
        os.system('kill $(lsof -t -i:50051)')
        sys.exit(1)

    def help_quit(self):
        print "syntax: quit",
        print "-- terminates the application"

    def do_disconnect(self, arg):

        try:
            del CLI.client_obj
            print "Disconnected from server"
        except:
            print "Sorry no connection to the server"
            cli.cmdloop()

    def help_get(self):
        print '''                  <<keyword>> <<keyword>     <<KEY_VALUE>>
				  <<get>> <<--key>> <<key>>  '''

    def help_put(self):
        print '''                  <<keyword>> <<keyword>     <<KEY_VALUE>>    <<keyword>> <<VALUE>>
				  <<put>> <<--key>> <<key>>  <<--value>>    <<value>>'''

    def help_disconnect(self):
        print ''' Syntax : <<disconnect>> - Disconnects from the server '''

   
cli = CLI()
cli.cmdloop()

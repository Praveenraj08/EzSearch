import cmd
import string, sys
import os
# import hello_client

class CLI(cmd.Cmd):
    def preloop(self):
     print "<<< connect host localhost port 50051 >>>"
    def postloop(self):
        print '''Connection closed '''

    def do_connect(self,arg1):
        print arg1
        l=arg1.split()
        if len(l)==4:
            if(l[0]=='--host'):
                if(l[1]=='localhost'):
                    if(l[2]=='--port'):
                        if(l[3]=='50051'):
                            print "perfect"
                            os.system('python client.py')
                        else:
                            print "Invalid port", l[3]
                            return
                    else:
                        print "Syntax error. << --port >>"
                        return
                else:
                    print "Invalid host"
                    return
            else:
                print "Syntax Error. << --host >>"
                return
        else:
            print "Invalid number of args"
            return

    

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = '--> '
    def help_connect(self):
        print '''                  <<keyword>> <<keyword>     <<IP>>    <<keyword>> <<Port number>>
                  <<connect>> <<--host>> <<localhost>>  <<--port>>    <<50051>>'''
   
    def do_quit(self, arg):
        os.system('fuser -k 50051/tcp')
        sys.exit(1)

    def help_quit(self):
        print "syntax: quit",
        print "-- terminates the application"
  

 #    # shortcuts
    do_disconnect = do_quit

    

#
# try it out

cli = CLI()
cli.cmdloop()
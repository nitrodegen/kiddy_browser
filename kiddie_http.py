import os,io,sys
from socket import *
from multiprocessing import Process
from kiddie_parser import Parser
class KiddieConnector(object):
    def __init__(self):
        print("Kiddie Connector was called.")
        self.port = 443
        self.hname = ""
        self.parser = Parser()
    
    """
        TODO:   
            implement POST request
            make socket faster  ( USE C!!!) 
            

    """
    def send_get_req(self,host,req):
        s = socket(AF_INET,SOCK_STREAM,IPPROTO_TCP)
        s.connect((host,self.port))
        print("Connected with port ",self.port)
        request = b"GET "+req.encode() +b" HTTP/1.0\r\nHost: b"+self.hname.encode()+b"\r\nConnection: close\r\n\r\n"
        data = b""
        s.send(request)
        while True:
            dat = s.recv(2048)
            if(len(dat) <=0):
                break
            else:
                data+=dat
        s.close()

        return data

    def send_post_req(self,host,req):
        print("Connecting with port ",self.port)


        s = socket(AF_INET,SOCK_STREAM,IPPROTO_TCP)
        s.connect((host,self.port))
        #print("Connected with port ",self.port)

        request = b"POST "+req.encode() +b" HTTP/1.0\r\nHost: b"+self.hname.encode()+b"\r\nConnection: close\r\n\r\n"
        data = b""
        s.send(request)
        while True:
            dat = s.recv(2048)
            if(len(dat) <=0):
                break
            else:
                data+=dat
        s.close()
        
        return data

    def fetch_web_data(self,ip,url,port,hname):
        self.port = port 
        
        if(len(url) <=0):
            url = "/"

        self.hname = hname
        
        
        resp = self.send_get_req(ip,url)
        resp = resp.decode().split("\r\n\r\n")[1]
        elements = self.parser.parse_html(resp)
        return elements

        

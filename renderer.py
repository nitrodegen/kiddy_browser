"""
    Kiddie Browser - basic GUI browser 
        @module_name: Renderer (Qt)
        @date:4.9.2022
        @author:nitrodegen
"""


import os,io,sys
from re import A
from xml.dom.minidom import Element
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
from PyQt5.QtWidgets import * 
from socket import *
from kiddie_http import * 
import random
KIDDIE_NOT_FOUND = 5
KIDDIE_RESTRICTED = 2

KIDDIE_INVALID_URL = 3
class Renderer(QMainWindow):
    def __init__(self):
        
        QMainWindow.__init__(self)
        self.visible =[]
        self.h = KiddieConnector()
        self.accessed=[]
        
        self.x = 0
        self.y = 20
        self.error = False
        self.setWindowTitle("Kiddie - Home Page")
        self.resize(1280,900)
        self.web_bar = QTextEdit("",self)
        self.web_bar.resize(1000,30)
        self.web_bar.move(125,30)
        self.web_bar.setStyleSheet("color:white;background-color:#272626")
        self.web_bar.setPlaceholderText("Search bar")
        self.web_bar.show()

         
        
        self.search_btn = QPushButton("Go!",self)
        self.search_btn.resize(80,30)
        self.search_btn.move(1150,30)
        self.search_btn.show()
        self.search_btn.clicked.connect(self.web_fetch)
        self.refresh_page = QPushButton(self)
        self.refresh_page.setStyleSheet("background-color:#272626")
        self.refresh_page.resize(50,30)
        self.refresh_page.move(50,30)
        self.refresh_page.show()
        self.refresh_page.setIcon(QIcon("./assets/b.png"))
        self.refresh_page.clicked.connect(self.web_fetch)


        self.load_home_page()


        self.show()



    def paintEvent(self,event):
        painter = QPainter(self)
       
        grad =QColor(50,50,50)
        painter.setPen(QPen(grad,  5, Qt.SolidLine))
        
        painter.setBrush(QBrush(grad))
        painter.drawRect(0, 00, 1920, 100)

    def load_home_page(self):
        self.hello = QLabel("\tWelcome to Kiddy!\n      web-browser built in 5 hours.",self)
        self.hello.resize(1000,300)
        self.hello.setFont(QFont("Arial",30))
        self.hello.show()
        self.hello.move(300,150)
 
        self.hello1 = QLabel("\tyou can see that because our design is 'revolutionary'\n\twe don't know why it is coded in python. don't ask plz",self)
        self.hello1.resize(1000,300)
        self.hello1.setFont(QFont("Arial",15))
        self.hello1.show()
        self.hello1.move(320,260)



        self.visible.append(self.hello)
        self.visible.append(self.hello1)



    def render_error_msg(self,t):
        self.error = True
        if(len(self.visible) > 0 ):
            for el in self.visible:
                el.clear()
        err_msg = "An error has occured." 
        if(t == KIDDIE_INVALID_URL):
            err_msg = "Invalid URL Provided. (missing dots) err_code: KIDDIE_INVALID_URL"
        if(t == KIDDIE_NOT_FOUND):
            err_msg = "Failed to connect to provided URL. err_code: KIDDIE_NOT_FOUND"
        if(t == KIDDIE_RESTRICTED):
            err_msg = "URL restricted. err_code: KIDDIE_RESTRICTED_URL"

        self.text_msg = QLabel(err_msg,self)
        self.text_msg.resize(1200,300)
        self.text_msg.move(300,0)
        self.text_msg.setFont(QFont("Arial",15)) 
        self.text_msg.show()
        self.visible.append(self.text_msg)

    def web_fetch(self): 
        for el in self.visible:
            el.clear()
            el.hide()
        self.setWindowTitle("/")

        url = self.web_bar.toPlainText()
        #self.web_bar.setText("")
      
        if(len(url)>0):
            if("/" not in url):
                url = url+"/"
            hostname = url.split("/")[0]
            
            port = 80 
            if("." not in url):
                self.render_error_msg(KIDDIE_INVALID_URL)
            
            if(":" in url):
                hostname = hostname.split(":")[0]

                url = url.split(":")
                port = int(url[1].split("/")[0])
                print("PORT:",port)

                url  = url[1].split("/")[1]
            
            
            if(self.error == False):
                ip = ""
                try:
                    tet = url.split("/")[0]
                    ip = gethostbyname(tet)
                    
                except gaierror as e:
                    self.render_error_msg(KIDDIE_NOT_FOUND)

                
                print(f"Connection to {ip} initiated ...")
                self.accessed.append(ip)

                parsed = self.h.fetch_web_data(ip,url,port,hostname)
                print(parsed)
                if(len(parsed) > 0 ):

                    if(parsed[0] == "RENDERED"):
                        for i in range(1,len(parsed)):
                            parse = parsed[i]
                            if(parse[0] == "IMG:"):
                                img = self.h.send_get_req(ip,parse[1])
                                img = img.split(b"\r\n\r\n")[1]
                                ff = parse[1].replace("/",".")
                                fname = f"{ff}"
                                f = open("./cache/"+fname,"wb")
                                f.write(img)
                                f.close()
                                self.lab = QLabel(self)
                                self.pixmap = QPixmap("./cache/"+fname)
                                self.lab.setPixmap(self.pixmap)
                                w = self.pixmap.width()
                                h = self.pixmap.height()
                                if(h >= 900 or w >=  1280):
                                    w/=2
                                    h/=2

                                self.lab.resize(w,h)
                                self.lab.move(self.x,self.y+170)
                                self.lab.show()
                                self.y+=h+30
                                self.visible.append(self.lab)
                                
                            if(parse[0] == "BODY:"):
                                self.setStyleSheet(parse[1])
                            if(parse[0] == "TITLE:"):
                                self.setWindowTitle(parse[1])     
                            if(parse[0] == "h1:"):
                                self.text = QLabel(parse[1],self)
                                
                                if(len(parse)>2):
                                    self.text.setStyleSheet(parse[3])
                                self.text.resize(len(parse[1])*100,300)
                                self.text.setFont(QFont("Times New Roman",15))

                                if(len(parse)>2):
                                    if("top:" in parse[3] or "left:" in parse[3]):
                                                x = parse[3].split("top:")[1]
                                                x = int(x.split(";")[0].replace("px",""))
                                                y = parse[3].split("left:")[1]
                                                y = int(y.split(";")[0].replace("px",""))
                                                self.text.move(y,x)
                                                self.x = y
                                                self.y =x+30
                                                print(self.x,self.y)


                                    else:
                                        self.text.move(self.x,self.y)
                                        print(self.x,self.y)
                                        self.y+=30
                                else:
                                        self.text.move(self.x,self.y)
                                        print(self.x,self.y)
                                        self.y+=30
                                
                                self.text.show()
                                self.visible.append(self.text)


                            if(parse[0] == "h2:"):
                                self.text = QLabel(parse[1],self)
                                
                                if(len(parse)>2):
                                    self.text.setStyleSheet(parse[3])
                                self.text.resize(len(parse[1])*100,300)
                                self.text.setFont(QFont("Times New Roman",14))

                                if(len(parse)>2):
                                    if("top:" in parse[3] or "left:" in parse[3]):
                                                x = parse[3].split("top:")[1]
                                                x = int(x.split(";")[0].replace("px",""))
                                                y = parse[3].split("left:")[1]
                                                y = int(y.split(";")[0].replace("px",""))
                                                self.text.move(y,x)
                                                self.x = y
                                                self.y =x+30

                                    else:
                                        self.text.move(self.x,self.y)
                                        print(self.x,self.y)
                                        self.y+=30
                                else:
                                        self.text.move(self.x,self.y)
                                        print(self.x,self.y)
                                        self.y+=30
                                
                                self.text.show()
                                self.visible.append(self.text)


                            if(parse[0] == "h3:"):
                                self.text = QLabel(parse[1],self)
                                
                                if(len(parse)>2):
                                    self.text.setStyleSheet(parse[3])
                                self.text.resize(len(parse[1])*100,300)
                                self.text.setFont(QFont("Times New Roman",13))
                                
                                if(len(parse)>2):
                                    if("top:" in parse[3] or "left:" in parse[3]):
                                                x = parse[3].split("top:")[1]
                                                x = int(x.split(";")[0].replace("px",""))
                                                y = parse[3].split("left:")[1]
                                                y = int(y.split(";")[0].replace("px",""))
                                                self.text.move(y,x)
                                                self.x = y
                                                self.y =x+30


                                    else:
                                        self.text.move(self.x,self.y)
                                        print(self.x,self.y)
                                        self.y+=30
                                else:
                                        self.text.move(self.x,self.y)
                                        print(self.x,self.y)
                                        self.y+=30
                                
                                self.text.show()
                                self.visible.append(self.text)


                            if(parse[0] == "p:"):
                                self.text = QLabel(parse[1],self)
                                
                                if(len(parse)>2):
                                    self.text.setStyleSheet(parse[3])
                                self.text.resize(len(parse[1])*100,300)
                                self.text.setFont(QFont("Times New Roman",11))

                                if(len(parse)>2):
                                    if("top:" in parse[3] or "left:" in parse[3]):
                                                x = parse[3].split("top:")[1]
                                                x = int(x.split(";")[0].replace("px",""))
                                                y = parse[3].split("left:")[1]
                                                y = int(y.split(";")[0].replace("px",""))

                                                self.text.move(y,x)
                                                self.x = y
                                                self.y =x+30
                                    else:
                                        self.text.move(self.x,self.y)
                                        print(self.x,self.y)
                                        self.y+=30
                                else:
                                        self.text.move(self.x,self.y)
                                        print(self.x,self.y)
                                        self.y+=30                            
                                self.text.show()

                                self.visible.append(self.text)

        else:
            print("Refresh kid")


if __name__ == "__main__":
    app =QApplication(sys.argv)
    win = Renderer()
    sys.exit(app.exec_())


import os,io,sys
from re import A




class Parser(object):
    def __init__(self):
        print("Kiddie _parser was called.")
        
    def parse_html(self,text):
        
        
        elements = ["RENDERED"] 
        lines = text.split("\n")
        is_html = False
        for i in range(5):
            if("<html>" in lines[i] or "<!DOCTYPE html>" in lines[i]):
                is_html= True
                break
        
        for i in range(len(lines)-5,len(lines)):
            if("</html>" in lines[i]):
                is_html=True
                break
            else:
                is_html = False


        if(is_html == True):
            #Task:seperate head and body from eachother, makes it easier to parse.
            body=[]
            head=[]
            for i in range(len(lines)):
                if("<head>" in lines[i]):
                    j = i+1 
                    while True:
                        if("</head>" in lines[j]):
                            break
                        if(j == len(lines)):
                            break
                        head.append(lines[j])
                        j+=1

                if("<HEAD>" in lines[i]):
                    j = i+1 
                    while True:
                        if("</HEAD>" in lines[j]):
                            break
                        if(j == len(lines)):
                            break
                        head.append(lines[j])
                        j+=1



                if("<body" in lines[i]):
                    if("style" in lines[i]):
                        data = lines[i].split("style=")[1].replace("\"","").replace(">","")
                        elements.append(["BODY:",data])

                    j = i+1 
                    while True:
                        if("</body>" in lines[j]):
                            break
                        if(j == len(lines)):
                            break
                        body.append(lines[j])
                        j+=1

                if("<BODY" in lines[i]):
                    if("style" in lines[i]):
                        data = lines[i].split("style=")[1].replace("\"","").replace(">","")
                        elements.append(["BODY:",data])

                    j = i+1 
                    while True:
                        if("</BODY>" in lines[j]):
                            break
                        if(j == len(lines)):
                            break
                        body.append(lines[j])
                        j+=1
                                          

             
            # **** PARSE HEAD ****

            for line in head:
                
                if("<title>" in line ):

                    
                    line = line.split("<title>")[1]
                    line = line.split("</title>")[0]
                    #print(line)
                    elements.append(["TITLE:",line])

                if("<TITLE>" in line ):

                    line = line.replace(" ","")
                    line = line.split("<TITLE>")[1]
                    line = line.split("</TITLE>")[0]
                    #print(line)
                    elements.append(["TITLE:",line])

            # **** PARSE BODY **** 
            """     
                for text stuff , you can only specify color , font-weight, font-family, left,top,right
            """
            for line in body:
                print(elements)

                if("<img" in line):
                    line = line.replace("<img","").replace(">","")
                    line = line.replace("src=","").replace("\"","")
                    elements.append(["IMG:",line.replace(" ","")])
                if("<h1" in line):
                    if("style" in line):
                        styles= line.split("style")[1]
                        text= styles.split(">")[1].replace("</h1","")
                        styles=styles.replace("=","").split(">")[0].replace("\"","")
                        elements.append(["h1:",text,"STYLE:",styles])
                        
                    else:
                            #print(line)
                            text = line.split("<h1>")[1].replace("</h1>","")
                            elements.append(["h1:",text])

                           
                if("<h2" in line):
                    if("style" in line):
                        styles= line.split("style")[1]
                        text= styles.split(">")[1].replace("</h2","")
                        styles=styles.replace("=","").split(">")[0].replace("\"","")
                        elements.append(["h2:",text,"STYLE:",styles])
                        
                    else:
                            #print(line)
                            text = line.split("<h2>")[1].replace("</h2>","")
                            elements.append(["h2:",text])

                if("<h3" in line):
                    if("style" in line):
                        styles= line.split("style")[1]
                        text= styles.split(">")[1].replace("</h3","")
                        styles=styles.replace("=","").split(">")[0].replace("\"","")
                        elements.append(["h3:",text,"STYLE:",styles])
                        
                    else:
                            #print(line)
                            text = line.split("<h3>")[1].replace("</h3>","")
                            elements.append(["h3:",text])


                if("<p" in line):
                    if("style" in line):
                        styles= line.split("style")[1]
                        text= styles.split(">")[1].replace("</p","")
                        styles=styles.replace("=","").split(">")[0].replace("\"","")
                        elements.append(["p:",text,"STYLE:",styles])
                        
                    else:
                            #print(line)
                            text = line.split("<p>")[1].replace("</p>","")
                            elements.append(["p:",text])
              

                
                if("<IMG" in line):
                    line = line.replace("<IMG","").replace(">","")
                    line = line.replace("src=","").replace("\"","")
                    elements.append(["IMG:",line.replace(" ","")])
                if("<H1" in line):
                    if("style" in line):
                        styles= line.split("style")[1]
                        text= styles.split(">")[1].replace("</H1","")
                        styles=styles.replace("=","").split(">")[0].replace("\"","")
                        elements.append(["h1:",text,"STYLE:",styles])
                        
                    else:
                            #print(line)
                            text = line.split("<H1>")[1].replace("</H1>","")
                            elements.append(["h1:",text])

                           
                if("<H2" in line):
                    if("style" in line):
                        styles= line.split("style")[1]
                        text= styles.split(">")[1].replace("</H2","")
                        styles=styles.replace("=","").split(">")[0].replace("\"","")
                        elements.append(["h2:",text,"STYLE:",styles])
                        
                    else:
                            #print(line)
                            text = line.split("<H2>")[1].replace("</H2>","")
                            elements.append(["h2:",text])

                if("<H3" in line):
                    if("style" in line):
                        styles= line.split("style")[1]
                        text= styles.split(">")[1].replace("</H3","")
                        styles=styles.replace("=","").split(">")[0].replace("\"","")
                        elements.append(["h3:",text,"STYLE:",styles])
                        
                    else:
                            #print(line)
                            text = line.split("<H3>")[1].replace("</H3>","")
                            elements.append(["h3:",text])


                if("<P" in line):
                    if("style" in line):
                        styles= line.split("style")[1]
                        text= styles.split(">")[1].replace("</P","")
                        styles=styles.replace("=","").split(">")[0].replace("\"","")
                        elements.append(["p:",text,"STYLE:",styles])
                        
                    else:
                            #print(line)
                            text = line.split("<P>")[1].replace("</P>","")
                            elements.append(["p:",text])
              

                       
#                    exit(1)
                    
        else:
            return text.split("\n")

        return elements


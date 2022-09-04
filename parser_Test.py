from kiddie_parser import Parser
import os,io,sys



text = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>hello</title>
</head>
<body style="background-color:black;">
    <h1 style="color:red;font-weight:bold;top:40px;left:20px;">Hello world!</h1>
    <h2 style="color:blue;font-weight:bold;top:70px;left:20px;" >Volim svoj zivot.</h2>
    <img src="{{url_for('static', filename='image.jpg')}}" >
    
</body>
</html>
"""
parser = Parser()
parser.parse_html(text)


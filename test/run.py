from flask import Flask
import flask
import os,io,sys
app = Flask(__name__)

@app.route('/')
def index():
    return flask.render_template("main.html")

app.run("0.0.0.0",port=4444,debug=True)

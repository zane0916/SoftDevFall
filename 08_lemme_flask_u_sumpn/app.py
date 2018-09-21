# Zane Wang
# SoftDev1 pd8
# K08 -- Fill Yer Flask
# 2018-09-20

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return 'Welcome to this first try! <br />  <a href="/second"> Who You? </a> <br />  <a href="/introduction"> Who Me? </a>'

@app.route("/second")
def speech():
    return "What is your name?"

@app.route("/introduction")
def introduce():
    return "Hi, my name is Zane." 

app.run()

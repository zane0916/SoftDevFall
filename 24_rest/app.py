#Team astro0 - Derek Song and Zane Wang
#SoftDev1 pd8
#K24 -- A RESTful Journey Skyward
#2018-11-13

from flask import Flask, render_template
app = flask(__name__)

@app.route("/")
def inform_user():
    return render_template("index.html", text = "Go to the relative route /nasa")

@app.route("/nasa")
def api_render():
    return render_template("index.html", text = "<h1> New Adventures in RESTful APIs: </h1><img src=''>")
    

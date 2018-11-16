# Zane Wang
# SoftDev1 pd8
# K25 -- Getting More REST
# 2018-11-14

import urllib
import json

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inform_user():
    return render_template("index.html", text = "None of these APIs require Keys! For Chuck Norris jokes, go to the relative route /chuck. For information from Studio Ghibli about Spirited Away, one of their most popular films, go to the relative route /ghibli. For information about the location of the International Space Station, go to the relative route /space")

@app.route("/chuck")
def gen_joke():
    url = "http://api.icndb.com/"
    query = "jokes/random"
    
    req = urllib.request.urlopen(url + query)
    info = req.read()

    dict = json.loads(info.decode('utf-8'))
    return render_template("index.html", text = dict["value"]["joke"])

@app.route("/ghibli")
def gen_movie():
    url = "https://ghibliapi.herokuapp.com/"
    query = "films/dc2e6bd1-8156-4886-adff-b39e6043af0c"

    req = urllib.request.urlopen(url + query)
    info = req.read()

    dict = json.loads(info.decode('utf-8'))
    return render_template("index.html", text = dict["description"])

@app.route("/space")
def gen_coord():
    url = "http://api.open-notify.org/iss-now.json"
    query = ""

    req = urllib.request.urlopen(url + query)
    info = req.read()

    dict = json.loads(info.decode('utf-8'))
    return render_template("index.html", text = "The timestamp currently is " + str(dict["timestamp"]) + ". The International Space Station is currently at a latitude of " + str(dict["iss_position"]["latitude"]) + " and a longitude of " + str(dict["iss_position"]["longitude"]) + ".")

if (__name__ == "__main__"):
    app.run()

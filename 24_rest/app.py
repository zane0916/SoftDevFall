#Team astro0 - Derek Song and Zane Wang
#SoftDev1 pd8
#K24 -- A RESTful Journey Skyward
#2018-11-13

import urllib
import json

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inform_user():
    req = urllib.request.urlopen("https://api.nasa.gov/planetary/apod?api_key=NL5NOjiOxQp40JmOqMbeQyAERaME2BjrB7JouJ1h")
    info = req.read()
    dict = json.loads(info.decode('utf-8'))
    return render_template("index.html", text = 'New Adventures in RESTful APIs', pic = dict['url'])

if (__name__ == "__main__"):
    app.run()

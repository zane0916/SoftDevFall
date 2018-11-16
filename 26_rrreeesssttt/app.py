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
    url = "https://api.pubg.com"
    query = "/shards/steam/players?filter[playerNames]=RapidIn"
    key = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI1MjE2NDkzMC1jYWNiLTAxMzYtMGQ5My02MTg0YzI3N2U2ZjEiLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNTQyMjYyMzM0LCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6Ii1jMTMzNGU1My00NzQ5LTQ3N2EtODk5OS03YjY2NjAxMDAxNWIifQ.5EZbPiuWEkDgcucs2UB6QSVM9eA5ejOsOYqRDFLBujI"
    
    req = urllib.request.urlopen(url + query)
    info = req.read()

    dict = json.loads(info.decode('utf-8'))
    return render_template("index.html", text = dict)

if (__name__ == "__main__"):
    app.run()

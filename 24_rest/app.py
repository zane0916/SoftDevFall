#Team astro0 - Derek Song and Zane Wang
#SoftDev1 pd8
#K24 -- A RESTful Journey Skyward
#2018-11-13

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def inform_user():
    return render_template("index.html", text = '<h1> New Adventures in RESTful APIs: </h1> <img src="https://earthengine.googleapis.com/api/thumb?thumbid=0d15ad8d2af6d8d0a6b083672514fae7&token=28818cafce7b74f5a6951b6051edd969">')

if (__name__ == "__main__"):
    app.run()

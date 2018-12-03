# Team ApumpkinPI - Anton Danylenko, Derek Song, Hui Min Wu, Zane Wang
# SoftDev1 pd8
# P01 -- ArRESTed Development
# 2018-11-28

import json, urllib, os, sqlite3

from flask import Flask, redirect, url_for, render_template, session, request, flash, get_flashed_messages

DB_FILE = "data/ApumpkinPI.db"

db = sqlite3.connect(DB_FILE)
c = db.cursor()

app = Flask(__name__)

def setupdb():
    #sets up database by creating tables that will exist in them
    #creates user tables
    command = "CREATE TABLE IF NOT EXISTS users(id INTEGER, user, pass)"
    c.execute(command)

    #creates favorite tables
    command = "CREATE TABLE IF NOT EXISTS favorites(id INTEGER, story)"
    c.execute(command)
    return c

@app.route("/")
def generate():
    return render_template("homepage.html")
    
'''
@app.route("/login")
    render_template("login.html")

@app.route("/register")
    render_template("register.html")

@app.route("/logout")
    render_template("logout.html")

@app.route("/movies")
    render_template("<>.html")

@app.route("/info")
    render_template("<>.html")
'''
    
@app.route("/search", methods = ["POST", "GET"])
def search():
    key = "b7503b8d"
    omdb = "http://www.omdbapi.com/?apikey=" + key + "&"
    mtitle = "t=" + request.form['search'] # gets the movie title that was searched and formats it for the api to work
    omdburl = omdb + mtitle
    x = urllib.request.urlopen(omdburl).read()
    mdata = json.loads(x)
    #print(mdata)
    args = {}
    args['title'] = mdata['Title']
    args['year'] = mdata['Year']
    args['actors'] = mdata['Actors']
    args['rating'] = mdata['Ratings']
    return render_template('movie.html', **args)

if (__name__ == "__main__"):
    app.run()

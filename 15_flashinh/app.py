# Team JayZ -- Johnson Li and Zane Wang
# SoftDev1 pd8
# K14 -- Do I Know You?
# 2018-10-01 M

import os
from flask import Flask, request, render_template, redirect, url_for, session, $

app = Flask(__name__)

# secret key for session
app.secret_key = os.urandom(32)
    
# hardcoded username and password
username = "JayZ"
password = "temp"

@app.route("/")
def login():
    # function for logging in, returns the home page template if credentials ar$
    # otherwise, it just renders the login page
    if username in session:
        return render_template("home.html", username = username)
    return render_template("login.html", error = "")

@app.route("/auth", methods=['GET', 'POST'])
def authenticate():
    usernameInput = request.form["user"]
    passwordInput = request.form["password"]

    # checks if credentials are correct
    # if they're correct add user to session and render home page
    # if not, they go back to login page
    if usernameInput == username and passwordInput == password:
        session[username] = username;
        return render_template("home.html", username = username)
    else:
        flash("Username or password is incorrect")
        return redirect(url_for("login"))

# remove user from session and redirect to login page
@app.route("/logout")
def logout():
    session.pop("JayZ")
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.debug = True
    app.run()

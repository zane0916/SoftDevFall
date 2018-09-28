# Zane Wang
# SoftDev1 pd1
# K13 -- Echo Echo Echo
# 2018-09-27

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")#renders form on the home page!
def hello_world():
    print(app)
    return render_template('NewForm.html')

@app.route("/auth")#after data is passed, code moves to /auth
def authenticate():
    print(app)
    print(request)
    print(request.args)
    print(request.args['username'])
    print(request.headers)
    #return statement returns a string that fulfills all parts of the homework
    return "Nice to meet you, " + request.args['username'] + "! The request method used to generate your username on this page is request.args with the key as username!"

if __name__ == "__main__":
    app.debug = True
    app.run()

# Team KraZyCodes -- Kendrick Liang and Zane Wang
# SoftDev pd8
# K10 -- Jinja Tuning
# 2018 - 09 - 22

from flask import Flask, render_template
from util import randomOccupation

app = Flask(__name__)

@app.route("/")
def output():
    return "Please head to occupations by adding /occupations at the end"
        
@app.route("/occupations")
def tablefy():
    return render_template("occupations.html",Title = 'Occupations', Heading = 'Table of Some Occupations', value = 'Possible option: ' + randomOccupation.randomOccupation(), col1 = 'Job Class', col2 = 'Percentage', result = dict)

if __name__ == "__main__":
    app.debug = True
    app.run()

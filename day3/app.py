''' 
    TEMPLATES INHERITANCE

PROBLEM we are gonna implement : Online Book Store

'''

from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("index.html")


@app.route("/viewbooks")
def viewbooks():
    return("viewbooks")

# pip install flask-sqlalchemy
'''
     Problem Statement :
        Store sample data in Db and fetch adn display the info in the page

'''
from flask import Flask


app = Flask(__name__)


@app.route("/")
def home_page():
    return ("HOME PAGE")

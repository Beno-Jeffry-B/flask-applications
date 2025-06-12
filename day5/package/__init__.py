from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sampleDB'

db = SQLAlchemy(app)

from package import routes






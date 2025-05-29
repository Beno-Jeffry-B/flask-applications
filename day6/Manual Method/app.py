from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#database req
app.config['SQLALCHEMEY_DATABASE_URI'] = "sqlite:///ItemDB.db"
db  = SQLAlchemy(app)




#define the model
class Items(db.Model):
    id = db.Column(db.Integer,primarykey=True)
    name = db.Column(db.String(30))
    price = db.Column(db.Float)
    


@app.route("/")
def sample_form():
    return render_template("index.html")
from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#database req
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///ItemDB.db"
db  = SQLAlchemy(app)




#define the model
class Items(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(30))
    price = db.Column(db.Float)
    

def create_db():
    
    with app.app_context():
        db.create_all()

    print("db created ")




@app.route("/")
def sample_form():
    return render_template("index.html")



if __name__ == "__main__":
    create_db()
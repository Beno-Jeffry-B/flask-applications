from flask import Flask,render_template,request,url_for,redirect
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




@app.route("/",methods = ['GET','POST'])   # By default, Flask only allows GET requests. or else "405 Method Not Allowed" wil occur
def sample_form():
    if request.method == "POST":
        name = request.form["input_name"]
        price = request.form["input_price"]

        item1 = Items(name=name,price=price)
        db.session.add(item1)
        db.session.commit()

        print("added to the Db successfully")

        return redirect(url_for('sample_form')) # redirect to GET after POST

    else:                                       
        return render_template("index.html")     # for GET or after redirect, just render form


if __name__ == "__main__":
    create_db()



#Scenario	    What to do
#GET request	Return form template (blank form)
#POST request   Process data,  redirect to GET route  (recommended)
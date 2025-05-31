from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField,DateField



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///SampleDB.db'
db = SQLAlchemy(app)

app.secret_key = "secret"


#defining model
class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    user_name = db.Column(db.String(30))
    email = db.Column(db.String(45))
    date_of_birth = db.Column(db.Date)
    password = db.Column(db.String(30))


#defining forms
class Signup_form(FlaskForm):
    user_name = StringField(label='name')
    email = StringField(label="email")
    date_of_birth = DateField(label="date")
    password = PasswordField(label="password")
    confirm_password = PasswordField(label="confirm_password")
    submit = SubmitField(label='submit') 

    
    
def database_creation():
    with app.app_context():
        db.create_all()





@app.route("/" , methods = ["POST" , "GET"])
def signup():
    signup_form  = Signup_form()
    
    if request.method == "POST":
        
        user_name = signup_form.user_name.data
        email   = signup_form.email.data
        date_of_birth   = signup_form.date_of_birth.data
        password    = signup_form.password.data
        confirm_password    = signup_form.confirm_password.data






        user1 = User(user_name =user_name, email=email , date_of_birth = date_of_birth ,password = password)
        
        print("user name : " , user_name)
        
            

    return render_template("index.html" , form = signup_form)
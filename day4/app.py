# pip install flask-sqlalchemy
'''
     Problem Statement :
        Store sample data in Db and fetch adn display the info in the page

'''
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime # for Date type

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sampleDB.db'
db = SQLAlchemy(app)

# This is a model which is Going to a table in our DB

class Student(db.Model):
    id   = db.Column(db.Integer , primary_key = True)
    name = db.Column(db.String(length = 30))
    gpa  = db.Column(db.Float)
    email = db.Column(db.String(50) , unique = True )
    dob  = db.Column(db.Date)  # Date is a type not method unlike mongo new Date()
    address = db.Column(db.Text)
    
    
@app.route("/")
def home_page():
    return ("HOME PAGE")






'''
Description
in python shell

When you're in the Python shell, Flask has no idea which app you're working with.so do below

>>> from app import app, db
>>> with app.app_context():
...     db.create_all()
...
>>>

>>> from app import Student

>>> s1 = Student(name = "jeffry" , gpa = 7.2 , email = "abce123@gmailcom" ,dob = date(2005,9,8) , address = "123-sample adress")

mistakes u should avoid in above line:
        ---> from datetime import date in shell to because we are using date()

>>> with app.app_context():
...  db.session.add(s1)                                                                                                           
...  db.session.commit()


>>> with app.app_context():        
...  students = Student.query.all()
...  for s in students:            
...   print(f"{s.id} - {s.name} - {s.email} - {s.dob} - {s.gpa} - {s.address}")


Always wrap DB calls (like add, commit, create_all, etc.) inside with app.app_context(): when running in shell or scripts outside Flask request handling.


but its hectic to do that in shell every time so for inserting write .py file and implement





Deleting DB is similar to deleting a file since Sqlite is a file based DB
    os.remove()  

'''
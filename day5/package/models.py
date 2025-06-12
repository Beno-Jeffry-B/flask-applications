
from package import db

class Student(db.Model):
    id   = db.Column(db.Integer , primary_key = True)
    name = db.Column(db.String(length = 30))
    gpa  = db.Column(db.Float)
    email = db.Column(db.String(50) , unique = True )
    dob  = db.Column(db.Date)  # Date is a type not method unlike mongo new Date()
    address = db.Column(db.Text)

    
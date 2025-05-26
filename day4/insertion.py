from app import app, db ,Student
from datetime import date

def insert_student():
    with app.app_context():
        s1 = Student(name = 'jeffry' , gpa = 6.9 , email = "abc123@gmail.com" , dob = date(2005,9,8) , address = "some sample address")
        db.session.add(s1)
        db.session.commit()

        print("Success..!")

#insert_student()

def display_student():
    with app.app_context():
        for s in Student.query.all():
            print(f"name : {s.name}\ngpa : {s.gpa}\nemail : {s.email}\nDate-of-Birth : {s.dob}\nAddress : {s.address}\n")

display_student()        
    

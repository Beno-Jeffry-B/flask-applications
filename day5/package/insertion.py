from package import app, db ,Student
from datetime import datetime

def insert_student(name,gpa,email,dob,address):
    with app.app_context():
        s = Student(name = name , gpa = gpa , email = email , dob = dob , address = address)
        db.session.add(s)
        db.session.commit()

        print("Successfuly inserted in DataBase..!")



def display_student():
    with app.app_context():
        for s in Student.query.all():
            print(f"name : {s.name}\ngpa : {s.gpa}\nemail : {s.email}\nDate-of-Birth : {s.dob}\nAddress : {s.address}\n")

       
    


if __name__ == "__main__":

    choice = None
    while(choice != 3):
        print("1 . Insert a student")
        print("2 . Display all students")
        print("3 . exit")
        choice = int(input("Enter the Choice:"))

        if(choice == 1 ):
            name =  input("Enter Name:")
            gpa =   float(input("enter gpa:"))
            email = input("enter the email:")
            dob_input = input("Enter DOB (YYYY-MM-DD): ")
            dob = datetime.strptime(dob_input, "%Y-%m-%d").date()  # parsing dob
            address = input("Enter Address :")
            insert_student(name,gpa,email,dob,address)

        elif(choice == 2 ):
            display_student()

        elif(choice == 3):
            break

        else:
            print("\ninvalid choice...try again\n")
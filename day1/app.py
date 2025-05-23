'''
    --> Hello world API
    --> Routing Basics
    --> Dynamic Routing(str and other types)

    running flask application
    
    method 1: 
    If your file name is other than app.py
    >> $env:FLASK_APP = "main.py"
    >> flask run 

    
    Alternate One-Liner for method 1 
    >> flask --app main.py run

    method 2: (direct flask run if file name is app.py)  
    >> flask run 

    Remove-Item Env:FLASK_APP   (make sure to do ...if u run prg using first method and trying out direct flask run
                                wont run so... remove $env first and run)


    For Debug mode on/off
    >> $env:FLASK_DEBUG=1
    >> flask run   

'''

from flask import Flask
app = Flask(__name__)

@app.route("/") #is called as decorators
def hello_world():
    return "hello!!!"

@app.route("/about")
def about():
    return "This is about page..." # here is where html pages are rendered..!

#dynamic routing

@app.route("/<u_name>")  #for str type
def name(u_name):
    return f"This is {u_name} page!"


@app.route("/<int:number>")  # <variable> name should be same as parameter name too...
def num(number):   
    return f"This is int type dynmic route of {number}"


@app.route("/<u_name>/<int:post_number>") 
def posts(u_name , post_number):   #The URL variables in the function parameters must be in the same order as in the route URL
    return f"This is {u_name}'s Post {post_number}"

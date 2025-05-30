'''
    > pip install flask-forms
    > pip install wtforms  
    
'''

from flask import Flask,render_template,request
from flask_wtf import FlaskForm

from wtforms import StringField,SubmitField,PasswordField


app = Flask(__name__)

app.secret_key = 'demo-key'   # for now

'''
    #  why we need this?
    It is required for CSRF protection (security).Without this, Flask-WTF will give an error.
    The token needs to be unique per user session and should be of large random value to make it difficult to guess.
'''


# defining Form class

class SimpleForm(FlaskForm):    #it inherits from FlaskForm
    name = StringField(label='name')
    password = PasswordField(label="password")
    confirm_password = PasswordField(label="confirm_password")
    submit = SubmitField(label='submit')



"""
| Flask-WTF Field            | Equivalent HTML Code                   |
| -------------------------- | -------------------------------------- |
| `StringField('Your Name')` | `<input type="text" name="name">`      |
| `SubmitField('Submit')`    | `<input type="submit" value="Submit">` |

"""



@app.route('/',methods = ['GET','POST'])   # When someone visits /, allow both GET and POST requests.
                                           # POST is triggered when you click the Submit button.
def form_page():
    form = SimpleForm()                     # an object of the form class — so we can render and use it. (refer OOP object creation)

    if request.method == "POST":
        print("Submitted name = ",form.name.data)

        
    return render_template("form.html",form = form)



'''

To add extra attributes

class SimpleForm(FlaskForm):
    name = StringField(label='name', render_kw={"placeholder": "Enter your name"})
    password = PasswordField(label="password", render_kw={"placeholder": "Enter password"})

Use render_kw


or in html


{{ form.name(placeholder="Enter your name") }}


can have as many args we want

like

{{ form.name(placeholder="Enter your name" , maxlength = 30)}}


'''
    







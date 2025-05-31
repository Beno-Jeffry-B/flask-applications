from flask import Flask, render_template,request,flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField,DateField,EmailField
from wtforms.validators import DataRequired ,Length ,EqualTo ,Email



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///SampleDB.db'
db = SQLAlchemy(app)

app.secret_key = "secret"


#defining model
class User(db.Model):
    id = db.Column(db.Integer,primary_key=True )
    user_name = db.Column(db.String(30), nullable = False)
    email = db.Column(db.String(45), nullable = False)
    date_of_birth = db.Column(db.Date, nullable = False)
    password = db.Column(db.String(30) ,nullable = False)


#defining forms
class Signup_form(FlaskForm):
    user_name = StringField(
                            label='name',render_kw = {"placeholder": "Enter your name"},
                            validators=[DataRequired(), Length(max=30)])

    email = StringField(
                            label="email",render_kw = {"placeholder": "Enter your Email"},
                            validators=[ DataRequired(),Email(),Length(max=45)])
    
    date_of_birth = DateField(  
                                label="date", render_kw = {"placeholder": "Enter your date of birth"},
                                 validators=[ DataRequired()]
                            )

    password = PasswordField(label="password",render_kw = {"placeholder": "Enter your password"},
                             validators=[ DataRequired(), Length(max=30)])

    confirm_password = PasswordField(label="confirm_password", render_kw = {"placeholder": "Enter your confirm_password"},
                                     validators=[ DataRequired(),  EqualTo('password' , message="Passwords must match") ,Length(max=30)] )

    submit = SubmitField(label='submit')
 

    
    
def database_creation():
    with app.app_context():
        db.create_all()





@app.route("/" , methods = ["POST" , "GET"])
def signup():
    signup_form  = Signup_form()
    
    if signup_form.validate_on_submit():
        
        user_name = signup_form.user_name.data
        email   = signup_form.email.data
        date_of_birth   = signup_form.date_of_birth.data
        password    = signup_form.password.data

        user1 = User(user_name =user_name, email=email , date_of_birth = date_of_birth ,password = password)

        db.session.add(user1)
        db.session.commit()
         
        flash("Successfully stored in DB" , "success")

    else:
        if request.method == "POST":
            for field_name, errors in signup_form.errors.items():
                for err in errors:
                    flash(f"{err}" ,"warning")



    return render_template("index.html" , form = signup_form)




if __name__ == "__main__":
    database_creation()
    app.run(debug=True)


    


''' 
     signup_form.errors.items()
     contains
        dict_items([('email', ['Invalid email address.']), ('date_of_birth', ['Not a valid date value.']), ('confirm_password', ['Field must be equal to password.'])])
when not all the validators works...



    for eg :  if we gave 
    if signup_form.validate_on_submiting():

    we will get the server error reason is because flask is intelligent enough of validates the things we given validate_on_ {name}
    this name submitting is not in forms that why we got server error so    

    now it will work { if signup_form.validate_on_submit(): }


    so the working mechanism is if block will check wheather all validators is satisfied and wheather it is POST ( when we click submit  ) ?
    if not returns false no output shown even in terminal no warning will be shown regarding the validations


    so we catch those warning in false blocl using form.errors

'''
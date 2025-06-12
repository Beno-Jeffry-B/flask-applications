from flask import Flask ,render_template , redirect , url_for ,session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from dotenv import load_dotenv
import os
load_dotenv()


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///SampleDb.db"
db = SQLAlchemy(app)



uri = os.getenv("DATABASE_URL")
if uri and uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://")  # Required fix
    
app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False





app.secret_key = 'qwertyuiop'



class User(db.Model):
    id = db.Column(db.Integer , primary_key=True)
    name = db.Column(db.String(50))

class sampleform(FlaskForm):
    name =  StringField(label='name')
    submit = SubmitField(label="submit")



with app.app_context():
    db.create_all()







@app.route("/", methods = ['GET', 'POST'])
def home_page():
    form = sampleform()
    if form.validate_on_submit():
        print("inside form")
        name = form.name.data
        user = User(name  = name )
        db.session.add(user)
        db.session.commit()
        print("stored in DB")
        return redirect(url_for('home_page'))
    return render_template('index.html' , form = form)


    
if __name__ == "__main__":
    app.run(debug=True)
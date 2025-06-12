
# flashes

from flask import Flask ,flash ,render_template

app = Flask(__name__)
app.secret_key = 'any-random-secret-key'  # required for session/flash


@app.route("/")
def home():
    flash("this is a flash message..!")
    return render_template("flashes.html")  #  You must need a template to read and show it.





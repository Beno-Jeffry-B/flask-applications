from package import app


@app.route("/")
def  home_page():
    return ("homepage!")


@app.route("/contact_us")
def  contact_us():
    return ("contact_us!")





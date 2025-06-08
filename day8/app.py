from flask import Flask, render_template, redirect, url_for, request, session
from forms import RegisterForm, LoginForm, RequestResetForm, ResetPasswordForm
from itsdangerous import URLSafeTimedSerializer
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'

# Fake DB (dictionary for simplicity)
users_db = {}

def generate_token(email):
    s = URLSafeTimedSerializer(app.config['SECRET_KEY'])
    return s.dumps({'email': email})

def verify_token(token, max_age=1800):
    s = URLSafeTimedSerializer(app.config['SECRET_KEY'])
    try:
        data = s.loads(token, max_age=max_age)
        return data['email']
    except Exception:
        return None

@app.route("/")
def home():
    return "Welcome! Go to /register or /login"

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        email = form.email.data
        password = generate_password_hash(form.password.data)
        users_db[email] = password
        print("Registered successfully!", "success")
        return redirect(url_for('login'))
    return render_template("register.html", form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user_pass = users_db.get(email)
        if user_pass and check_password_hash(user_pass, password):
            print("Login successful!", "success")
        else:
            print("Invalid credentials", "danger")
    return render_template("login.html", form=form)

@app.route("/forgot-password", methods=["GET", "POST"])
def forgot_password():
    form = RequestResetForm()
    if form.validate_on_submit():
        email = form.email.data
        if email in users_db:
            token = generate_token(email)
            reset_url = url_for('reset_token', token=token, _external=True) # which makes the token str into links(URL)
            print(f"🔗 Reset URL (simulated email): {reset_url}") # This has to be Mailed
            print("Password reset link sent! (check console)", "info") 
        else:
            print("Email not found", "danger")
    return render_template("forgot_password.html", form=form)

@app.route("/reset-password/<token>", methods=["GET", "POST"])
def reset_token(token):
    email = verify_token(token)
    if not email:
        print("Invalid or expired token.", "danger")
        return redirect(url_for('forgot_password'))

    form = ResetPasswordForm()
    if form.validate_on_submit():
        new_password = generate_password_hash(form.password.data)
        users_db[email] = new_password
        print("Password updated successfully!", "success")
        return redirect(url_for('login'))
    return render_template("reset_token.html", form=form)

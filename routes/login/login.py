from flask import Blueprint, render_template, session, request, redirect, url_for
from filmfan import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

home = Blueprint("home", __name__, static_folder="static", template_folder="templates")

# Define the User model
class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# Define the Regisseur model
class Regisseur(db.Model):
    # Define your model here
    pass

# Database setup
db.create_all()

# The user_loader decorator allows flask-login to load the current user
# and grab their id.
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# Login route
@home.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("form_email")
        password = request.form.get("form_password")
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            # Here you can set session variables if needed
            return redirect(url_for('home.dashboard'))
        else:
            return "Invalid email or password"
    return render_template("login.html")

# Registration route
@home.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form.get("form_email")
        username = request.form.get("form_username")
        password = request.form.get("form_password")
        user = User.query.filter_by(email=email).first()
        if user:
            return "Email already registered. Please login."
        new_user = User(email=email, username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('home.login'))
    return render_template("register.html")

# Dashboard route
@home.route("/dashboard")
def dashboard():
    # Here you can implement the logic for rendering the user dashboard
    return render_template("dashboard.html")


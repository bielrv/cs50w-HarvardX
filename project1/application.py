import os
import requests
from flask import Flask, session, render_template, request
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from datetime import datetime

# from flask.ext.heroku import Heroku

os.getcwd()

# res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "0yOQWbyRCLpwoPzvLkCe9Q", "isbns": "9781632168146"})
# print(res.json())

app = Flask(__name__)

# Check for environment variable
# if not os.getenv("DATABASE_URL"):
#    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
# engine manages communitations between the flask app and the postgres db
engine = create_engine(os.getenv("DATABASE_URL"))
# scoped_session allows to manage different sessions for different people
db = scoped_session(sessionmaker(bind=engine))

# Set "homepage" to index.html
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register",methods=["POST"])
def register():
    # Form variables
    username = request.form.get("username")
    email = request.form.get("email")
    password = request.form.get("password")
    repassword = request.form.get("repassword")
    dt = datetime.now()

    # Print for debugging purposes
    _username_exists = username_exists(username)
    _email_exists = email_exists(email)

    print("usernames_available:",username_exists(username))
    print("email_available:",email_exists(email))

    # Check if everything is ok
    if not _username_exists and not _email_exists:
        # Insert new user to accounts
        db.execute("Insert into accounts (username,password,email,created_on) values (:username,:password,:email,:created_on)",
        {"username":username,"email":email,"password":password,"created_on":dt})
        # Print for debugging purposes
        print(username+" "+email+" "+password+" registered")
        # Commit changes to database
        db.commit()
        # Render registered page
        text = username + "! You have been successfully registered!"
    elif _username_exists:
        text = "Username not available..."
    elif _email_exists:
        text = "Email not available..."
    else:
        text = "Unkown error..."
    return render_template("registered.html",text=text)

@app.route("/login",methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    if user_match(username,password):
        return render_template("hello.html",name=username)
    elif not username_exists(username):
        text = "Username " + username + " does no exist"
        return render_template("index.html",text=text)
    else:
        text = "User and password do not match"
        return render_template("index.html",text=text)

@app.route("/hello",methods=["POST"])
def hello():
    name = request.form.get("name")
    return render_template("hello.html",name=name)

# Method that checks if username exists
def username_exists(username):
    return 0 != db.execute("Select count(*) from accounts where username = :username",
    {"username":username}).scalar()

# Method that checks if email exists
def email_exists(email):
    return 0 != db.execute("Select count(*) from accounts where email = :email",
    {"email":email}).scalar()

# Method that checks if username and password match
def user_match(username,password):
    return 1 == db.execute("Select count(*) from accounts where username = :username and password = :password",
    {"username":username,"password":password}).scalar()

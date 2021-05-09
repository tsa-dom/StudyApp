from app import app
from flask import redirect, request, session, render_template
from werkzeug.security import check_password_hash, generate_password_hash
from os import urandom
import access as db
import validate

def create_sessions(username):
    session["username"] = username
    session["id"] = db.get_user_id(username)[0]
    session["csrf_token"] = urandom(16).hex()
    session["material_id"] = -1
    session["chapter_id"] = -1


@app.route("/signup", methods=["GET"])
def signup():
    return render_template("signup.html")

@app.route("/login", methods=["GET"])
def login():
    return render_template("login.html")

@app.route("/signup", methods=["POST"])
def create():
    username = request.form["username"]
    password = request.form["password"]
    confirmation = request.form["confirmation"]
    print(validate.equal(username, password))
    if validate.username(username) and validate.password(password) and validate.equal(password, confirmation):
        password_hash = generate_password_hash(request.form["password"])
            
        if db.create_user(username, password_hash):
            create_sessions(username)
            return redirect("/")

    else:
        redirect("/")

    return redirect("/signup")

@app.route("/login", methods=["POST"])
def auth():
    username = request.form["username"]
    user = db.user_in_db(username)
    if user == None:
        return redirect("/login")

    password = request.form["password"]
    hash_password = user[2]

    if check_password_hash(hash_password, password):
        create_sessions(username)
        return redirect("/")
    else:
        return redirect("/login")

@app.route("/logout", methods=["GET"])
def logout():
    del session["username"]
    del session["id"]
    del session["csrf_token"]
    del session["material_id"]
    del session["chapter_id"]
    return redirect("/")
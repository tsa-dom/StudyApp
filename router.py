from app import app
from flask import redirect, request, session, render_template
from werkzeug.security import check_password_hash, generate_password_hash
from os import urandom
import access as db

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/signup", methods=["GET"])
def signup():
    return render_template("signup.html")

@app.route("/login", methods=["GET"])
def login():
    return render_template("login.html")

@app.route("/new", methods=["GET"])
def new_material():
    return render_template("create.html")

@app.route("/signup", methods=["POST"])
def create():
    username = request.form["username"]
    password_hash = generate_password_hash(request.form["password"])
            
    if db.create_user(username, password_hash):
        session["username"] = username
        session["id"] = db.get_user_id(username)[0]
        session["csrf_token"] = urandom(16).hex()
        session["material_id"] = -1
        session["chapter_id"] = -1
        return redirect("/")

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
        session["username"] = username
        session["id"] = db.get_user_id(username)[0]
        session["csrf_token"] = urandom(16).hex()
        session["material_id"] = -1
        session["chapter_id"] = -1
        print(session["csrf_token"])
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

@app.route("/materials", methods=["GET"])
def all_materials():
    result = db.material_content()
    materials = result.fetchall()
    return render_template("materials.html", materials=materials, title="Kaikki oppimateriaalit")

@app.route("/materials/my", methods=["GET"])
def user_materials():
    result = db.material_content(session["id"])
    materials = result.fetchall()
    return render_template("materials.html", materials=materials, title="Omat oppimateriaalit")

@app.route("/materials", methods=["POST"])
def create_material():
    if (request.form["csrf"] != session["csrf_token"]):
        abort(403)
    name = request.form["name"]
    description = request.form["description"]
    category = request.form["category"]
    if db.create_material(name, description, "Empty", session["id"], category) == False:
      return redirect("/new")

    return redirect("/materials")


@app.route("/materials/<int:material_id>")
def material(material_id):
    try:
        session["username"]
        session["material_id"] = material_id
        material = db.user_material(session["id"], material_id)
        chapters = db.chapters_by_id(material_id)
        owner = False
        if material != None:
            owner = True
        else:
            material = db.material_by_id(material_id)

        return render_template("material.html",
            owner=owner,
            name=material[1],
            contents=material[3],
            rows=len(material[3].splitlines()),
            chapters=chapters
        )
                    
    except:
        return redirect("/login")

@app.route("/materials/contents", methods=["POST"])
def change_contents():
    try:
        if (request.form["csrf"] != session["csrf_token"]):
            abort(403)
        contents = request.form["content_area"]
        db.update_contents(session["material_id"], contents)
        return redirect("/materials/" + str(session["material_id"]))
    except:
        return redirect("/")

@app.route("/chapters", methods=["POST"])
def add_chapter():
    try:
        if (request.form["csrf"] != session["csrf_token"]):
            abort(403)
        name = request.form["chapter_name"]
        content = request.form["chapter_content"]
        db.create_chapter(name, session["material_id"], content)
        return redirect("/materials/" + str(session["material_id"]))
    except:
        return redirect("/")

@app.route("/chapters/<int:chapter_id>")
def chapter(chapter_id):
    try:
        session["username"]
        session["chapter_id"] = chapter_id
        chapter = db.user_chapter(session["id"], session["material_id"], chapter_id)
        owner = False
        if chapter != None:
            owner = True
        else:
            chapter = db.chapter_by_id(chapter_id)

        return render_template("chapter.html",
            owner=owner,
            name=chapter[1],
            contents=chapter[3],
            rows=len(chapter[3].splitlines())
        )
    except Exception as ex:
        print(ex)
        return redirect("/materials")

@app.route("/chapters/contents", methods=["POST"])
def change_content():
    try:
        if (request.form["csrf"] != session["csrf_token"]):
            abort(403)
        contents = request.form["content_area"]
        db.chapter_contents(session["chapter_id"], contents)
        return redirect("/chapters/" + str(session["chapter_id"]))
    except:
        return redirect("/")
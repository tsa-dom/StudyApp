from app import app
from flask import redirect, request, session, render_template
import access as db

def identify_user(request):
    if (request.form["csrf"] != session["csrf_token"]):
        abort(403)

@app.route("/materials/new", methods=["GET"])
def new_material():
    return render_template("create.html")

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
    identify_user(request)
    name = request.form["name"]
    description = request.form["description"]
    category = request.form["category"]
    if db.create_material(name, description, "\r\r\r\r\r", session["id"], category) == False:
      return redirect("/new")

    return redirect("/materials")


@app.route("/materials/<int:material_id>")
def material(material_id):
    try:
        session["username"]
        session["material_id"] = material_id
        material = db.user_material(session["id"], material_id)
        chapters = db.chapters_by_id(material_id)
        feedback = db.get_feedback(material_id)
        likes = db.like_status(material_id, session["id"])
        if likes == None:
            likes = False
        elif likes[0] == 0:
            likes = False
        else:
            likes = True

        print(likes)
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
            chapters=chapters,
            feedback=feedback,
            likes=likes
        )
                    
    except:
        return redirect("/login")

@app.route("/materials/contents", methods=["POST"])
def change_contents():
    try:
        identify_user(request)
        contents = request.form["content_area"]
        db.update_contents(session["material_id"], contents)
        return redirect("/materials/" + str(session["material_id"]))
    except:
        return redirect("/")

@app.route("/materials/remove/<int:material_id>", methods=["POST"])
def delete_material(material_id):
    if material_id == session["material_id"]:
        db.drop_material(material_id)
    return redirect("/materials/my")

@app.route("/materials/name/<int:material_id>", methods=["POST"])
def change_name(material_id):
    try:
        identify_user(request)
        name = request.form["name"]
        db.update_material_name(session["material_id"], name)
        return redirect("/materials/" + str(material_id))
    except:
        return redirect("/")

@app.route("/materials/feedback/<int:material_id>", methods=["POST"])
def add_feedback(material_id):
    try:
        identify_user(request)
        db.add_feedback(material_id, session["id"], request.form["feedback"])
        return redirect("/materials/" + str(material_id))
    except:
        return redirect("/")

@app.route("/materials/like/<int:material_id>/<int:like_value>", methods=["POST"])
def like(material_id, like_value):
    try:
        identify_user(request)
        db.like(material_id, session["id"], like_value - 1)
        return redirect("/materials/" + str(material_id))
    except:
        return redirect("/")
from app import app
from flask import redirect, request, session, render_template
import access as db

def identify_user(request):
    if (request.form["csrf"] != session["csrf_token"]):
        abort(403)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

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

@app.route("/search")
def search_material():
    return render_template("search.html")

@app.route("/search/result", methods=["POST"])
def search_result():
    try:
        key = request.form["keyword"]
        param = request.form["search_param"]
        materials = None
        if param == 'name':
            materials = db.materials_by_name(key)
        elif param == 'author':
            materials = db.materials_by_author(key)
        elif param == 'tag':
            materials = db.materials_by_category(key)
        return render_template("materials.html", materials=materials, title="Materiaalit hakusanalla " + key)
    except:
        return redirect("/")
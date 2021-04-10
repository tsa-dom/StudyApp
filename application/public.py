from flask import render_template, session, redirect, request

class Public:

    def __init__(self, app, dao):
        self.app = app
        self.dao = dao

        @app.route("/materials", methods=["GET"])
        def all_materials():
            result = dao.material_content()
            materials = result.fetchall()
            return render_template("materials.html", materials=materials, title="Kaikki oppimateriaalit")

        @app.route("/materials/my", methods=["GET"])
        def user_materials():
            result = dao.material_content(session["id"])
            materials = result.fetchall()
            return render_template("materials.html", materials=materials, title="Omat oppimateriaalit")

        @app.route("/materials", methods=["POST"])
        def create_material():
            name = request.form["name"]
            description = request.form["description"]
            category = request.form["category"]
            if dao.create_material(name, description, "Empty", session["id"], category) == False:
                return redirect("/new")

            return redirect("/materials")


        @app.route("/materials/<int:material_id>")
        def material(material_id):
            try:
                session["username"]
                session["material_id"] = material_id
                material = dao.user_material(session["id"], material_id)
                if material != None:
                    return render_template("material.html",
                        owner=True,
                        name=material[1],
                        contents=material[3],
                        rows=len(material[3].splitlines())
                    )
                else:
                    material = dao.material_by_id(material_id)
                    return render_template("material.html",
                        name=material[1],
                        contents=material[3],
                        rows=len(material[3].splitlines())
                    )
                    
            except:
                return redirect("/login")

        @app.route("/materials/contents", methods=["POST"])
        def change_contents():
            try:
                session["username"]
                contents = request.form["content_area"]
                dao.update_contents(session["material_id"], contents)
                return redirect("/materials/" + str(session["material_id"]))
            except:
                return redirect("/")
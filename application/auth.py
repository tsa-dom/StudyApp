from flask import redirect, request, session
from werkzeug.security import check_password_hash, generate_password_hash

class Auth:

    def __init__(self, app, dao):
        self.app = app
        self.dao = dao

        @app.route("/signup", methods=["POST"])
        def create():
            username = request.form["username"]
            password_hash = generate_password_hash(request.form["password"])
            
            if dao.create_user(username, password_hash):
                session["username"] = username
                session["id"] = dao.get_user_id(username)[0]
                return redirect("/")

            return redirect("/signup")

        @app.route("/login", methods=["POST"])
        def auth():
            username = request.form["username"]
            user = dao.user_in_db(username)
            if user == None:
                return redirect("/login")

            password = request.form["password"]
            hash_password = user[2]

            if check_password_hash(hash_password, password):
                session["username"] = username
                session["id"] = dao.get_user_id(username)[0]
                return redirect("/")
            else:
                return redirect("/login")

        @app.route("/logout", methods=["GET"])
        def logout():
            del session["username"]
            del session["id"]
            return redirect("/")
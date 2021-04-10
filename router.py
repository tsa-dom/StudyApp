from flask import render_template

class Router:

    def __init__(self, app):
        self.app = app

        @app.route("/", methods=["GET"])
        def index():
            return render_template("main.html")

        @app.route("/signup", methods=["GET"])
        def signup():
            return render_template("signup.html")

        @app.route("/login", methods=["GET"])
        def login():
            return render_template("login.html")

        @app.route("/new", methods=["GET"])
        def new_material():
            return render_template("create.html")
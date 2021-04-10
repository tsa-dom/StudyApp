from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv
from router import Router
from public import Public
from auth import Auth
from dao.user_dao import UserDao
from dao.material_dao import MaterialDao

app = Flask(__name__)
app.secret_key = getenv("SECRET")
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DB_KEY")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
user_dao = UserDao(db)
material_dao = MaterialDao(db)

router = Router(app)
auth = Auth(app, user_dao)
public = Public(app, material_dao)
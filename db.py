from app import app
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app.secret_key = getenv("SECRET")
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DB_KEY")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
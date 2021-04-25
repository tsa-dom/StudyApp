from flask import Flask

app = Flask(__name__)

import router
import auth
import materials
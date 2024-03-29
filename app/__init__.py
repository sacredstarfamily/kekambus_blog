from flask import Flask # Import the Flask class from the flask module
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_migrate import Migrate
# Create an instance of Flask called app which will be the central object
app = Flask(__name__)
app.config.from_object(Config)
# import the routes to the app
db = SQLAlchemy(app)
mirgrate = Migrate(app, db)
from . import routes, models
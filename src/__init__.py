import click
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:password@127.0.0.1:3307/books'
db = SQLAlchemy(app)

"""
Import blueprints for cli
"""
from src.models import *
import src.commands.db_cli as db_cli
import src.blueprints as blueprints

app.register_blueprint(blueprints.home)
app.register_blueprint(db_cli.db_blueprint)


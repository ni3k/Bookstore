import click
import os
from flask import Blueprint
from src import db, Books

db_blueprint = Blueprint('db', __name__)

@db_blueprint.cli.command('init')
def init():
   db.create_all()

@db_blueprint.cli.command('insert:all')
def insertAll():
   PATH = os.path.join(os.getcwd(), 'rawbooks')
   files = os.scandir(PATH)
   for file in files:
      print(file.name)
      db.session.add(Books(name = file.name))
   db.session.commit()
   files.close()

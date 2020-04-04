import click
import os
from flask import Blueprint, render_template, request, send_file
from src import db, Books

'''
This blueprint will handle download, search, and get flow
idk why i named it home
'''
home = Blueprint('home', __name__)

@home.route('/')
def home_url():
   return render_template('home.html')

@home.route('/search', methods=('GET', 'POST'))
def search_url():
   if request.method == 'GET':
      return render_template('home.html')
   elif request.method == 'POST':
      searched = request.form.get('search')
      likeThis = f"%{searched}%"
      books = Books.query.filter(Books.name.like(likeThis)).all()
      print(books)
      return render_template('searches.html', books=books, searched=searched)

@home.route('/books/<id>', methods=('GET',))
def books_url(id):
   if request.method == 'GET':
      book = Books.query.get(id)
      if not book:
         return render_template('404.html')
      filename = os.path.join(os.getcwd(), 'rawbooks', book.name)
      return send_file(filename, attachment_filename=book.name, as_attachment=True)
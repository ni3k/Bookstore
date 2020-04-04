# Bookstore
*disclaimed: This is only a playground, nothing serious, idk if it will be of any help to you.*


Bookstore is a python/flask webserver helping to easily host a bunch of books.

## Installation

activate venv, etc or don't (your choice)

after:

```bash
pip install -r requirements.txt
```

## Usage
first of all populate your books in rawbooks folder

second: copy .env.example -> .env

thirst:
```bash
$ flask db init
$ flask db insert:all # this will insert all titles from rawbooks in db
$ flask run
```


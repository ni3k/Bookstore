from src import db
from sqlalchemy import ForeignKey


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), unique=True, nullable=False)

    def __repr__(self):
        return f'<Books {self.name}>'
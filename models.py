from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)


"""Models for Blogly."""

class User(db.Model):
    __tablename__ = 'users'

    def __repr__(self):
        u = self
        return f"<User id= {u.id} first_name = {u.first_name} last = {u.last_name} image = {u.image}>"

    id = db.Column(db.Integer,
                   primary_key = True,
                   autoincrement = True)

    first = db.Column(db.String(30),
                      nullable = False)

    last = db.Column(db.String(30),
                      nullable = False)

    image = db.Column(db.String)

    def greet(self):
        return f"Hello, I am {u.first}"
"""Blogly application."""

from flask import Flask, redirect, request, render_template, session, flash
from models import db, connect_db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()

#showing home page...............
@app.route("/")
def main():
    users = User.query.all()
    return render_template('home.html', users = users)

#posting from home page..........
@app.route("/", methods = ["POST"])
def add_user():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    image = request.form["image"] 

    new_user = User(first = first_name, last = last_name, image = image)
    db.session.add(new_user)
    db.session.commit()
    return redirect (f"/{new_user.id}")

#showimg detailed info of user.....
@app.route("/<int:user_id>")
def details(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('details.html', user = user)

@app.route("/<int:user_id>", methods=['POST'])
def detailed(user_id):
    user = User.query.get_or_404(user_id)
    first_name = request.form["new_first_name"]
    last_name = request.form["new_last_name"]
    image = request.form["new_image"]

    user = User(first = first_name, last = last_name, image = image)
    db.session.add(user)
    db.session.commit() 
    return render_template('details.html', user = user)
#star of edit....................

@app.route("/<int:user_id>/edit")
def edit(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('/edit.html', user = user)
   
@app.route("/<int:user_id>/edit", methods = ["POST"])
def apply_edit(user_id):
    user = User.query.get_or_404(user_id)
    
    return render_template ("details.html", user = user)
#end of editing....................

#start of deleting.................
@app.route("/<int:user_id>/delete")
def delete(user_id):
    user = User.query.get_or_404(user_id)
    User.query.filter(User.id == user_id).delete()
    db.session.commit()
    users = User.query.all()
    return render_template('home.html', users = users)
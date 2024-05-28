from flask_app import app
from flask import Flask, redirect, render_template, request, session, jsonify
from flask_app.models.user import User
from flask_app.models.book import Book


@app.route("/")
def dashboard():
    users = User.get_all()
    # return dojos
    return render_template("dashboard.html", users=users)


@app.route("/new/user", methods=["POST"])
def newUser():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
    }
    User.create(data)
    return redirect("/")


@app.route("/user/<int:id>")
def users(id):
    data = {"id": id}
    user = User.get_user_by_id(data)
    books = Book.get_books()
    fav_books = User.get_all_fav_books(data)
    return render_template("user.html", user=user, books=books, fav_books=fav_books)

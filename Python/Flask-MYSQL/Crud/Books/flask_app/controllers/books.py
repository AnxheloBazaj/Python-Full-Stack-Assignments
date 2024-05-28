from flask_app import app
from flask import Flask, redirect, render_template, request, session, jsonify
from flask_app.models.user import User
from flask_app.models.book import Book


@app.route("/books/")
def books():
    users = User.get_all()
    books = Book.get_books()
    return render_template("books.html", users=users, books=books)


@app.route("/add/book/", methods=["POST"])
def newBooks():
    data = {
        "title": request.form["title"],
        "num_of_pages": request.form["num_of_pages"],
    }
    Book.create(data)
    return redirect(request.referrer)


@app.route("/book/<int:id>")
def book(id):
    data = {"id": id}
    users = User.get_all()
    book = Book.get_book_by_id(data)
    fav_users = Book.get_all_user_fav(data)
    return render_template("book.html", book=book, users=users, fav_users=fav_users)


@app.route("/add/to_fav/", methods=["POST"])
def addToFav():
    data = {"user_id": request.form["user_id"], "book_id": request.form["book_id"]}
    Book.addFav(data)
    return redirect(request.referrer)

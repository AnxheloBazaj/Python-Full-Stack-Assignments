from flask_app import app
from flask import Flask, render_template, redirect, request
from flask_app.models.user import User


@app.route("/")
def add():
    return render_template("create.html")


@app.route("/users")
def show():
    users = User.get_all()

    return render_template("read.html", users=users)


@app.route("/create_user", methods=["POST"])
def create_user():

    User.create(request.form)
    return redirect("/users")


@app.route("/delete_user/<int:user_id>")
def delete(user_id):
    data = {"id": user_id}
    User.delete(data)
    return redirect("/users")


@app.route("/edit/<int:id>")
def edit(id):

    data = {"id": id}
    user = User.get_user_by_id(data)
    return render_template("edit.html", user=user)


@app.route("/update/<int:id>", methods=["POST"])
def update(id):
    data = {
        "id": id,
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
    }
    User.update(data)
    return redirect("/profile/" + str(id))


@app.route("/profile/<int:id>")
def profile(id):
    data = {"id": id}
    user = User.get_user_by_id(data)
    return render_template("profile.html", user=user)

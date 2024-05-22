from flask_app import app
from flask import Flask, redirect, render_template, request, session, jsonify
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja


@app.route("/dojo/ninjas/<int:id>")
def ninjas(id):
    data = {"id": id}
    dojo = Dojo.get_dojo_by_id(data)
    ninjas = Ninja.get_ninjas_by_id(data)
    return render_template("ninjas.html", ninjas=ninjas, dojo=dojo)


@app.route("/add/ninja")
def add():
    return render_template("add.html", dojos=Dojo.get_all())


@app.route("/add/ninja/", methods=["POST"])
def addNinja():
    data = {
        "dojo_id": request.form["dojo_id"],
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "age": request.form["age"],
    }
    Ninja.create(data)
    return redirect("/dojo/ninjas/" + str(data["dojo_id"]))


@app.route("/edit/ninja/<int:id>")
def edit(id):
    data = {"id": id}
    ninja = Ninja.get_ninja_by_id(data)
    return render_template("editNinja.html", ninja=ninja)


@app.route("/update/ninja/<int:id>", methods=["POST"])
def update(id):
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "age": request.form["age"],
        "id": id,
    }
    Ninja.update(data)
    dojo_id = Ninja.get_ninja_by_id(data)

    return redirect("/dojo/ninjas/" + str(dojo_id["dojo_id"]))


@app.route("/delete/ninja/<int:id>")
def delete(id):
    data = {"id": id}
    Ninja.delete(data)

    return redirect(request.referrer)

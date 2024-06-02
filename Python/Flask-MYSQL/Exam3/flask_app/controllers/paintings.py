from flask_app import app
from flask_app.models.painting import Painting
from flask_app.models.user import User
from flask import Flask, render_template, redirect, request, session, flash


@app.route("/painting/new")
def addPainting():
    if "user_id" not in session:
        return redirect("/")
    data = {"id": session["user_id"]}
    loggeduser = User.get_user_by_id(data)
    return render_template("addShow.html", loggeduser=loggeduser)


@app.route("/add/painting", methods=["POST"])
def createPainting():
    if "user_id" not in session:
        return redirect("/")
    if not Painting.validate_painting(request.form):
        return redirect(request.referrer)
    data = {
        "title": request.form["title"],
        "price": request.form["price"],
        "quantity": request.form["quantity"],
        "description": request.form["description"],
        'user_id': session['user_id']
    }
    Painting.create(data)
    return redirect("/")


@app.route("/painting/<int:id>")
def viewShow(id):
    if "user_id" not in session:
        return redirect("/")
    data = {"painting_id": id, "id": session["user_id"]}
    painting = Painting.get_painting_by_id(data)
    loggeduser = User.get_user_by_id(data)
    # usersWhoLiked = Show.get_users_who_liked(data)
    return render_template("show.html", painting=painting, loggeduser=loggeduser)#, usersWhoLiked=usersWhoLiked, numOfLikes=len(Show.get_users_who_liked(data)))


@app.route("/delete/painting/<int:id>")
def deletePainting(id):
    if "user_id" not in session:
        return redirect("/")
    data = {"painting_id": id, "id": session["user_id"]}
    painting = Painting.get_painting_by_id(data)
    loggeduser = User.get_user_by_id(data)
    if painting["user_id"] == loggeduser["id"]:
        # Show.delete_all_likes(data)
        Painting.delete_painting(data)
    return redirect("/")


@app.route("/painting/edit/<int:id>")
def editShow(id):
    if "user_id" not in session:
        return redirect("/")
    data = {"painting_id": id, "id": session["user_id"]}
    painting = Painting.get_painting_by_id(data)
    if not painting:
        return redirect('/')
    loggeduser = User.get_user_by_id(data)
    if painting['user_id']!= loggeduser['id']:
        return redirect('/')
    return render_template("editShow.html", painting=painting, loggeduser=loggeduser)


@app.route("/update/painting/<int:id>", methods=["POST"])
def updateShow(id):
    if "user_id" not in session:
        return redirect("/")
    data = {"painting_id": id, "id": session["user_id"]}
    painting = Painting.update_paintig(data)
    if not painting:
        return redirect('/')
    loggeduser = User.get_user_by_id(data)
    if painting['user_id']!= loggeduser['id']:
        return redirect('/')
    if (
        len(request.form["title"]) < 1
        or len(request.form["price"]) < 1
        or len(request.form["quantity"]) < 1
        or len(request.form["description"]) < 1
    ):
        flash("All fields required", "allRequired")
        return redirect(request.referrer)
    updateData={
        'title': request.form['title'],
        'price': request.form['price'],
        'quantity': request.form['quantity'],
        'description': request.form['description'],
        'show_id':id
    }
    if not Painting.validate_painting(updateData):
        return redirect(request.referrer)
    Painting.update_paintig(updateData)
    return redirect('/painting/'+ str(id))


# @app.route('/like/<int:id>')
# def addLike(id):
#     if 'user_id' not in session:
#         return redirect('/')
#     data = {
#         'show_id': id,
#         'id': session['user_id']
#     }
#     usersWhoLiked = Show.get_users_who_liked(data)
#     if session['user_id'] not in usersWhoLiked:
#         Show.addLike(data)
#         return redirect(request.referrer)
#     return redirect(request.referrer)

# @app.route('/unlike/<int:id>')
# def removeLike(id):
#     if 'user_id' not in session:
#         return redirect('/')
#     data = {
#         'show_id': id,
#         'id': session['user_id']
#     }    
#     Show.removeLike(data)
        
#     return redirect(request.referrer)

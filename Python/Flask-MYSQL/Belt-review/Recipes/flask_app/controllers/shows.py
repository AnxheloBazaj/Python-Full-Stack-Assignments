from flask_app import app
from flask_app.models.show import Show
from flask_app.models.user import User
from flask import Flask, render_template, redirect, request, session, flash


@app.route("/shows/new")
def addshow():
    if "user_id" not in session:
        return redirect("/")
    data = {"id": session["user_id"]}
    loggeduser = User.get_user_by_id(data)
    return render_template("addShow.html", loggeduser=loggeduser)


@app.route("/add/show", methods=["POST"])
def createShow():
    if "user_id" not in session:
        return redirect("/")
    if not Show.validate_show(request.form):
        return redirect(request.referrer)
    data = {
        "title": request.form["title"],
        "network": request.form["network"],
        "releaseDate": request.form["releaseDate"],
        "description": request.form["description"],
        'user_id': session['user_id']
    }
    Show.create(data)
    return redirect("/")


@app.route("/show/<int:id>")
def viewShow(id):
    if "user_id" not in session:
        return redirect("/")
    data = {"show_id": id, "id": session["user_id"]}
    show = Show.get_show_by_id(data)
    loggeduser = User.get_user_by_id(data)
    usersWhoLiked = Show.get_users_who_liked(data)
    return render_template("show.html", show=show, loggeduser=loggeduser, usersWhoLiked=usersWhoLiked, numOfLikes=len(Show.get_users_who_liked(data)))


@app.route("/delete/show/<int:id>")
def deleteShow(id):
    if "user_id" not in session:
        return redirect("/")
    data = {"show_id": id, "id": session["user_id"]}
    show = Show.get_show_by_id(data)
    loggeduser = User.get_user_by_id(data)
    if show["user_id"] == loggeduser["id"]:
        Show.delete_all_likes(data)
        Show.delete_show(data)
    return redirect("/")


@app.route("/show/edit/<int:id>")
def editShow(id):
    if "user_id" not in session:
        return redirect("/")
    data = {"show_id": id, "id": session["user_id"]}
    show = Show.get_show_by_id(data)
    if not show:
        return redirect('/')
    loggeduser = User.get_user_by_id(data)
    if show['user_id']!= loggeduser['id']:
        return redirect('/')
    return render_template("editShow.html", show=show, loggeduser=loggeduser)


@app.route("/update/show/<int:id>", methods=["POST"])
def updateShow(id):
    if "user_id" not in session:
        return redirect("/")
    data = {"show_id": id, "id": session["user_id"]}
    show = Show.get_show_by_id(data)
    if not show:
        return redirect('/')
    loggeduser = User.get_user_by_id(data)
    if show['user_id']!= loggeduser['id']:
        return redirect('/')
    if (
        len(request.form["title"]) < 1
        or len(request.form["network"]) < 1
        or len(request.form["releaseDate"]) < 1
        or len(request.form["description"]) < 1
    ):
        flash("All fields required", "allRequired")
        return redirect(request.referrer)
    updateData={
        'title': request.form['title'],
        'network': request.form['network'],
        'releaseDate': request.form['releaseDate'],
        'description': request.form['description'],
        'show_id':id
    }
    if not Show.validate_show(updateData):
        return redirect(request.referrer)
    Show.update_show(updateData)
    return redirect('/show/'+ str(id))


@app.route('/like/<int:id>')
def addLike(id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'show_id': id,
        'id': session['user_id']
    }
    usersWhoLiked = Show.get_users_who_liked(data)
    if session['user_id'] not in usersWhoLiked:
        Show.addLike(data)
        return redirect(request.referrer)
    return redirect(request.referrer)

@app.route('/unlike/<int:id>')
def removeLike(id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'show_id': id,
        'id': session['user_id']
    }    
    Show.removeLike(data)
        
    return redirect(request.referrer)

from flask import Flask, render_template, redirect, request
from flask_app import app

# import the class from friend.py
from flask_app.models.friend import Friend

# @app.route("/")
# def index():
#     # call the get all classmethod to get all friends
#     friends = Friend.get_all()
#     print(friends)
#     return render_template("index.html", all_friends = friends)


# @app.route('/friends/create', methods=["POST"])
# def create_friend():
#     # First we make a data dictionary from our request.form coming from our template.
#     # The keys in data need to line up exactly with the variables in our query string.
#     data = {
#         "first_name": request.form["first_name"],
#         "last_name": request.form["last_name"],
#         "occupation": request.form["occupation"]
#     }
#     # We pass the data dictionary into the save method from the Friend class.
#     Friend.save(data)
#     # Don't forget to redirect after saving to the database.
#     return redirect('/')
@app.route("/")
def index():
    # calling the get_all method from the friends.py
    all_friends = Friend.get_all()
    # passing all friends to our template so we can display them there
    return render_template("index.html", friends=all_friends)


@app.route("/friend/show/<int:friend_id>")
def show(friend_id):
    # calling the get_one method and supplying it with the id of the friend we want to get
    friend = Friend.get_one(friend_id)
    return render_template("show_friend.html", friend=friend)


@app.route("/friends/create", methods=["POST"])
def create():
    Friend.save(request.form)
    return redirect("/")

@app.route('/edit')
def edit():
    return render_template('edit.html')
@app.route("/friends/update", methods=["POST"])
def update():
    Friend.update(request.form)
    return redirect("/")
@app.route('/friends/delete/<int:friend_id>')
def delete(friend_id):
    Friend.delete(friend_id)
    return redirect('/')

from flask_app import app
from flask import Flask, redirect, render_template, request,session, jsonify
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/')
def dashboard():
    dojos = Dojo.get_all()
    # return dojos
    return render_template('dashboard.html', dojos=dojos)


@app.route('/new/dojo', methods=['POST'])
def newDojo():
    data= {
        "name":request.form["name"]
    }
    Dojo.create(data)
    return redirect('/')

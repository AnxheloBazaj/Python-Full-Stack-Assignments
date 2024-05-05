from flask_app import app
from flask import render_template , request, redirect, session # added request
@app.route('/')
def index():

    if 'visit' not in session:
        session['visit'] = 0
    else:
        session['visit'] +=1
    return render_template("index.html", visit=session['visit'])
@app.route('/count')
def process():
    return redirect('/')
@app.route('/reset')
def delete():
    session.clear()
    return redirect('/')


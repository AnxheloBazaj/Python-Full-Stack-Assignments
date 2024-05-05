from flask_app import app
from flask import render_template , request, redirect, session
from random import randint



@app.route('/')
def random():
    if 'random_number' not in session:
        num = randint(1, 100)
        session['random_number'] = num
    elif 'gues' not in session:
        session['gues'] = session.get('gues', 0)
    return render_template('form.html', random_num= session['random_number'], gues= session['gues'])


@app.route('/guess',methods = ['POST'] )
def gues():
    session['gues'] = request.form['gues']
    return redirect('/')

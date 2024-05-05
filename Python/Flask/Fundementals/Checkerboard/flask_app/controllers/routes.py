from flask_app import app
from flask import render_template
@app.route("/")
def display(row=8, col=8, color1="purple", color2="black"):
    
    return render_template("index.html", row=row, colum=col, color1=color1, color2=color2)
@app.route("/<int:row>")
def display1(row, col=8, color1="purple", color2="black"):
    
    return render_template("index.html", row=row, colum=col, color1=color1, color2=color2)

@app.route("/<int:row>/<int:col>")
def display2(row, col, color1="orange", color2="yellow"):
    return render_template("index.html", row=row, colum=col, color1=color1, color2=color2)

@app.route("/<int:row>/<int:col>/<color1>/<color2>")
def display3(row, col, color1, color2):
    return render_template("index.html", row=row, colum=col, color1=color1, color2=color2)
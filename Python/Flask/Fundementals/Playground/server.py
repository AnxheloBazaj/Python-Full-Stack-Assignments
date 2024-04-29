from flask import Flask, render_template  
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return render_template("index.html")

@app.route('/play/<int:num>')          # The "@" decorator associates this route with the function immediately following
def play(num):
    return render_template("index2.html", num = num)
@app.route('/play/<int:num>/<colour>')          # The "@" decorator associates this route with the function immediately following
def play2(num, colour="green"):
    return render_template("index3.html", num = num, colour=colour)
# Return the string 'Hello World!' as a response
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)
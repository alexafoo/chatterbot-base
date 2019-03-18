from flask import Flask, render_template, request, redirect
from flask_socketio import SocketIO
app = Flask(__name__)

#default page
@app.route("/")
def home():
    return render_template("index.html");

#submit chat
@app.route('/submit', methods = ['POST'])
def submit():
    text_data = request.form['text']
    print("The text is '" + text_data + "'")
    return redirect('/');

if __name__ == "__main__":
    app.run(debug=True)
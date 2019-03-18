from flask import Flask, render_template, request, redirect
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'chatbotbeepboop'
socketio = SocketIO(app)

#default page
@app.route("/")
def home():
    return render_template("index.html");

#msg received
def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)

#submit chat
@app.route('/submit', methods = ['POST'])
def submit():
    text_data = request.form['text']
    print("The text is '" + text_data + "'")
    return redirect('/');

if __name__ == "__main__":
    app.run(debug=True)
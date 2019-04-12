import gevent.monkey
gevent.monkey.patch_all()
from flask import Flask, render_template, request, redirect
from flask_socketio import SocketIO
import sqlite3
from chatterbot import ChatBot
#

bot = ChatBot(
    'Terminal',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'Sorry, I do not understand',
            'maximum_similarity_threshold': 0.8


        },
        {
            'import_path': 'chatterbot.logic.BestMatch',

        }
 #       'chatterbot.logic.TimeLogicAdapter',

    ],
    read_only=True,
    database_uri='sqlite:///Data.db')



app = Flask(__name__)
app.config['SECRET_KEY'] = 'chatbotbeepboop'
socketio = SocketIO(app)

#default page
@app.route("/")
def sessions():
    return render_template("index.html");

#msg received
def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@socketio.on('my event')
def handle_my_custom_event(text, methods=['GET', 'POST']):
    print('received my events_test: ' + str(text))
    server_inp = text['message']
    ans_get = bot.get_response(server_inp)
    print(ans_get)
    #socketio.emit('my response', ans_get, callback=messageReceived);
    #socketio.emit('my response', text, callback=messageReceived)
    socketio.emit('my response', {'question': server_inp, 'message': str(ans_get)})
    engine.say(str(ans_get))


#submit chat
@app.route('/submit', methods = ['POST'])
def submit():
    text_data = request.form['message']
    print("The text is '" + text_data + "'")
    return redirect('/');

# Uncomment the following lines to enable verbose logging
# import logging
# logging.basicConfig(level=logging.INFO)

# Create a new instance of a ChatBot



if __name__ == "__main__":
    socketio.run(app, debug=True)
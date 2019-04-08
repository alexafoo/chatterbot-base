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
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.BestMatch'
    ],
    database_uri='sqlite:///database.db'
)

conn = sqlite3.connect('ddh.db', check_same_thread=False)
c = conn.cursor()

def access_db(question):
    print(question)
    c.execute("select answers from cases1 where questions='%s'" %question)
    #c.execute("select * from cases1")
    res = c.fetchall()
    print(res)
    res1=(str(res))
    res1 = res1[3:-4]
    #print(res1)
    #print("tt")
    return res1


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
    server_inp=text['message']
    ans_get=access_db(server_inp)
    print(ans_get)
    #socketio.emit('my response', ans_get, callback=messageReceived);
    #socketio.emit('my response', text, callback=messageReceived)
    socketio.emit('my response',{ 'question': server_inp, 'message': ans_get });

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

def access_db(question):
    print(question)
    c.execute("select answers from cases1 where questions='%s'" %question)
    res = c.fetchall()
    print(res)
    res1=(str(res))
    res1 = res1[3:-4]
    return res1

if __name__ == "__main__":
    socketio.run(app, debug=True)
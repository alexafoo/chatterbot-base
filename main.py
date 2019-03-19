from flask import Flask, render_template, request, redirect
from flask_socketio import SocketIO
import sqlite3
from chatterbot import ChatBot

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










# Uncomment the following lines to enable verbose logging
# import logging
# logging.basicConfig(level=logging.INFO)

# Create a new instance of a ChatBot

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

conn = sqlite3.connect('ddh.db')
c = conn.cursor()
#if init == 0:
#c.execute("CREATE TABLE cases1 (questions str, answers str)")
#else :
#c.execute('INSERT INTO cases1 VALUES("Hola","Hola back")')
#c.execute('INSERT INTO cases VALUES("What is your name","IDK")')
#c.execute('INSERT INTO cases VALUES("exit","See ya back")')
print("Please enter your question, type 'y' or 'n' to continue")
if input()!= 'n':
    print("Please enter your question.")
    var1=input()
    print("Please enter your answer.")
    var2=input()
    c.execute("INSERT INTO cases1 VALUES(?,?)", (var1, var2))
    conn.commit()

print('Type something to begin...')
botName = "I don't have a name yet"
# The following loop will execute each time the user enters input
while True:
    try:
        user_input = input()


        bot_response = "see ya!"
        c.execute("select answers from cases1 where questions='%s'"%user_input)
   #     sql_parameterized_query = """select answers from cases where questions = %s """
   #     c.execute(sql_parameterized_query, user_input)
        results = c.fetchone()
        almost=(str(results))
        print(almost[2:-3])
        print  (bot_response)

     #   elif user_input == c.execute("select * from cases where questions=: user_input()", {botName: "select * from cases where answers"}):

    #        print(botName)
        #elif user_input == "How may I call you":
         #   print(botName)
        #else:
        #    print("I don't understand")
       #     bot_response = bot.get_response(user_input)

       # print(bot_response)
    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit,):
        break


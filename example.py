import sqlite3
from chatterbot import ChatBot

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
var1=input()
var2=input()

c.execute("INSERT INTO cases1 VALUES(%?,?)", (var1, var2))
conn.commit()

print('Type something to begin...')
botName = "I don't have a name yet"
# The following loop will execute each time the user enters input
while True:
    try:
        user_input = input()

        if user_input == var1:
            bot_response = "see ya!"
            c.execute("select answers from cases1 where questions = ?",var1)
       #     sql_parameterized_query = """select answers from cases where questions = %s """
       #     c.execute(sql_parameterized_query, user_input)
            results = c.fetchall()
            print(results)
            print  (bot_response)
            break
     #   elif user_input == c.execute("select * from cases where questions=: user_input()", {botName: "select * from cases where answers"}):

    #        print(botName)
        elif user_input == "How may I call you":
            print(botName)
        else:
            print("I don't understand")
       #     bot_response = bot.get_response(user_input)

       # print(bot_response)
    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit,):
        break

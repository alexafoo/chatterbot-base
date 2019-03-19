import sqlite3
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import logging


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

print('Type your question here, type (quit) to end the conversation')
botName = "I don't have a name yet"
# The following loop will execute each time the user enters input
while True:
    try:
        user_input = input()

        if user_input != 'quit':
            c.execute("select questions from cases1 where questions='%s'"%user_input)
            res = c.fetchall()
            res1=(str(res))
            res1 = res1[3:-4]
            if user_input != 'quit' and user_input!= res1:
                print(res1)
                print("Sorry,I don't understand")
            else :
                c.execute("select answers from cases1 where questions='%s'"%user_input)
                results = c.fetchone()
                almost=(str(results))
                print(almost[2:-3])
        elif user_input == 'quit':
            print("See ya")
            break









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

#logging.basicConfig(level=logging.INFO)

#chatbot = ChatBot('Example Bot')

# Start by training our bot with the ChatterBot corpus data
#trainer = ChatterBotCorpusTrainer(chatbot)

#trainer.train(
#    'chatterbot.corpus.english'
#)

# Now let's get a response to a greeting
#response = chatbot.get_response('How are you doing today?')
#print(response)

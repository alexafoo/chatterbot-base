import sqlite3
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import logging


# Uncomment the following lines to enable verbose logging
# import logging
# logging.basicConfig(level=logging.INFO)

# Create a new instance of a ChatBot

bot = ChatBot(
    'Terminal',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'Sorry, I do not understand',
            'maximum_similarity_threshold': 0.95


        },
        {
            'import_path': 'chatterbot.logic.BestMatch',

        }
 #       'chatterbot.logic.TimeLogicAdapter',

    ],
    read_only=True,
    database_uri='sqlite:///Data.db')


conn = sqlite3.connect('Data.db')
# print out the table
c = conn.execute("SELECT id, text from statement")
for row in c:
    print("id =", row[0], "| text =", row[1])
# ask the user for deletion
print("Press 'd' to delete one of the question, enter anything else to skip this process")
delete = input()
while delete == 'd':
    print("Please enter the ID for the question you want to delete")
    var = input()
    print("Please enter the ID for the answer you want to delete")
    var2 = input()
    c.execute("DELETE from statement where id ='%s'" % var)
    c.execute("DELETE from statement where id ='%s'" % var2)
    conn.commit()
    print("Enter d to delete another question, enter anything else to skip")
    delete = input()
# ask the user for modification
print("Press 'm' to modify one of the question, enter anything else to skip this process")
modify = input()
while modify == 'm':
    print("Please enter the block ID for making changes")
    var = input()
    c = conn.execute("SELECT text from statement where id ='%s'" % var)
    res = c.fetchall()
    res1 = (str(res))
    res1 = res1[3:-4]
    print("You want to change |  %s " % res1, "| into")
    newI = input()
    c.execute("Update statement set text = ? where id = ?", (newI, var))
    conn.commit()
    print("Enter m to make more modifications, enter anything else to skip")
    modify = input()



#if init == 0:
#c.execute("CREATE TABLE cases1 (questions str, answers str)")
#else :
#c.execute('INSERT INTO cases1 VALUES("Hola","Hola back")')
#c.execute('INSERT INTO cases VALUES("What is your name","IDK")')
#c.execute('INSERT INTO cases VALUES("exit","See ya back")')

print('--------------Training--------------')
trainer = ListTrainer(bot)
#print("How many key questions do we have for this conversation?")
#points = int(input())
#cp = [0 for x in range(points)]
#for x in cp:
#    print(x)
while True:
    print("Please enter the question you want to add to start, type 'end' to skip")
    question = input()
    if question == 'end':
        break
    print("What is the response for", question)
    answer = input()
    trainer.train([
        question,
        answer,
    ])
    print("type 'end' to quit, type 'a' if you think another question leads to the same answer")
    print("type anything else to ")
    checker = input()
    while checker == 'a':
        print("what question do you think have the same answer for ", answer)
        question = input()
        trainer.train([
            question,
            answer,
        ])
        print("type 'end' to quit, type 'a' if you think another question leads to the same answer")
        checker = input()
    if checker == 'end':
        break
print('-----------------testing-----------------')
print('Type your question here, type (quit) to end the conversation')
# The following loop will execute each time the user enters input
while True:
    try:
        user_input = input()
        if user_input == 'quit':
            break
        bot_response = bot.get_response(user_input)

        print(bot_response),








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


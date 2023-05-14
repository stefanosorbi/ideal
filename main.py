import telegram
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, ApplicationBuilder
import random

with open('try.txt', 'r') as f:
    text = f.read()
    paragraphs = text.split("\n\n")

# create an updater object
application = ApplicationBuilder().token('6193378141:AAEs-3Kkybzf7CJ7I9B07bR0x75KiyakxhY').build()

# define a function to handle the /start command
async def start(update, context):
    await context.bot.send_message(chat_id=update.message.chat_id, text='Hello! I am your bot. How can I assist you?')

# define a function to handle text messages
async def text(update, context):
    message_text = update.message.text.lower() # convert message text to lowercase
    message = "Sorry, I don't know, what are you talking about"
    for t in paragraphs:
        print(t.split("\n"))
        if message_text in t.split("\n")[0]:
            message = t.split("\n")[1]
            break         
    await context.bot.send_message(chat_id=update.message.chat_id, text=message)

# create handlers for the /start command and text messages
start_handler = CommandHandler('start', start)
text_handler = MessageHandler(filters.TEXT, text)

# add the handlers to the updater
application.add_handler(start_handler)
application.add_handler(text_handler)

# start the bot
application.run_polling()

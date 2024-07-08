import os
import telebot
file = open('shopping_list.txt')
array = str(file.readlines())
BOT_TOKEN = os.environ.get('SHOPPING_LIST_BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, array)

bot.infinity_polling()
from telebot import TeleBot, types
import json
import os
import time

TOKEN = '6764832972:AAE2fYXU1mQYTiIhse4NZzMJepO2BGzA-1E'
bot = TeleBot(TOKEN)

with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)



@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to YourBot! Type /info to get more information.")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for item in data.keys():
        markup.add(item)
    bot.send_message(message.chat.id, "Select an option:", reply_markup=markup)

@bot.message_handler(commands=['reload'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for item in data.keys():
        markup.add(item)
    bot.send_message(message.chat.id, "Select an option:", reply_markup=markup)

@bot.message_handler()
def button(message):
    try:
        photos = []
        for photo in os.listdir(data[message.text]):
            photos.append(open(data[message.text] + photo, 'rb'))
        for photo in photos:
            bot.send_photo(message.chat.id, photo)
            photo.close()
    except:
        bot.send_message(message.chat.id, "eblan?")
        bot.send_message(message.chat.id, "Ладно, дам тебе шанс. Если выпадет больше 3, то ты не eblan")
        dice = bot.send_dice(message.chat.id)
        time.sleep(4)
        if dice.dice.value < 4:
            bot.send_message(message.chat.id, "Все таки ты eblan")
        elif dice.dice.value == 6:
            bot.send_message(message.chat.id, "Ты не eblan, ты шестерка получается")
        else:
            bot.send_message(message.chat.id, "Ладно, ты не eblan")


bot.infinity_polling()
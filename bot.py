from re import TEMPLATE
import telebot
import time
import qrcode
import random
import requests
from textblob import TextBlob

# img = qrcode.make("https://prnt.sc/214gue0")
# img.save("QR1")

from telebot.types import Message
bot_token = "5026220606:AAE7bScX__ezhFKbOpJi9FYLKR85Vtcvl7Y"

bot = telebot.TeleBot(token=bot_token)

files = {'photo':open(r'D:\assignment\project-learning\Telegrambot\qr_.png','rb')}


def find_at(msg):
    for text in msg:
        if '@' in text:
            return text

@bot.message_handler(commands=['start'])
def mainone(message):
    bot.reply_to(message,"Hello Human,If you want to know more about me use '/help'.")
    




# @bot.message_handler(commands=['start'])
# def send_welcome(message):
#     bot.reply_to(message,'Hello Human!')

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message,'To activte,send a telegram username with prefix as @')

@bot.message_handler(func=lambda msg: msg.text is not None and '@' in  msg.text)
def at_answer(message):
    texts = message.text.split() 
    at_text = find_at(texts)
    new  = "https://instagram.com/{}".format(at_text[1:])
    bot.reply_to(message,new)
    # bot.reply_to(message,"Happy?")
    img = qrcode.make(new)
    img.save("qr_.png")
    resp = requests.post('https://api.telegram.org/bot5026220606:AAE7bScX__ezhFKbOpJi9FYLKR85Vtcvl7Y/sendPhoto?chat_id=1246580961',files=files)
    bot.send_message(message.chat.id,"hi")
    print(resp.status_code)
    bot.send_photo("/qr")
   
@bot.message_handler(commands= ["chat"])
def chatbot(message):
    bot.reply_to(message,"I am ULTRON,the ultimate robot made to handle peace..altho iam not in my original coutume but iam in a good mood so ask me whatever you want to!")

@bot.message_handler(commands= ["okay"])
def chatbot(message):
    bot.reply_to(message,"I am ULTRON,the ultimate robot made to handle peace..altho iam not in my original coutume but iam in a good mood so ask me whatever you want to!")


# @bot.message_handler(commands=["hello","hi","hey"])
# def rep(message):
#     bot.reply_to(message,mainone(message))



while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(2)
import os
import telebot

bot_token = "5026220606:AAE7bScX__ezhFKbOpJi9FYLKR85Vtcvl7Y"

bot = telebot.TeleBot(token=bot_token)


@bot.message_handler(commands = ['yo'])
def greet(message):
    bot.reply_to(message,"hey yo")

@bot.message_handler(commands=['hello'])
def hello(message):
    bot.send_message(message.chat.id,"hekllo")

bot.polling()
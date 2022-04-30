import os
import telebot

bot_token = "5026220606:AAE7bScX__ezhFKbOpJi9FYLKR85Vtcvl7Y"

bot = telebot.TeleBot(token=bot_token)


@bot.message_handler(commands = ['Greet'])
def greet(message):
    bot.reply_to(message,"hey yo")


bot.polling()

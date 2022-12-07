import telebot
from weather_getter import weather_request, get_weather
from config import API_KEY

# MY_API_KEY = 'secret'
# bot = telebot.TeleBot(MY_API_KEY)

bot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=['start'])
def greet(message):
    docs = "Type /help to see what I can do !\n"
    bot.reply_to(message, docs)


@bot.message_handler(commands=['help'])
def greet(message):
    # print(message.text)
    docs = " type /Greet to say hi to bot\n\n" \
           "type 'weather' + <city_name> to get the weather of a city \n\n"
    bot.reply_to(message, docs)


@bot.message_handler(commands=['Greet'])
def greet(message):
    bot.reply_to(message, "hi!")


@bot.message_handler(func=weather_request)
def reply_weather(message):
    city = (message.text.split()[1:])
    city1 = ' '.join(city) + ' weather'
    reply = get_weather(city1)
    bot.reply_to(message, reply)


bot.polling()

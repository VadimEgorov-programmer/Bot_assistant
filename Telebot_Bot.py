import telebot
import requests
import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
WEATHER_TOKEN = os.getenv("WEATHER_TOKEN")

bot = telebot.TeleBot(token=TELEGRAM_TOKEN)
keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Какая погода за вашим окном?')


@bot.message_handler(commands=['start'])
def start_message(message):
    text_start_message = 'Привет {0.first_name}!, я {1.first_name}! Умею показывать погоду в одном' \
                         ' из существующих городов. В областях не ориентируюсь.'.format(message.from_user, bot.get_me())
    bot.send_message(message.chat.id, text_start_message, reply_markup=keyboard1)


@bot.message_handler(content_types=["text"])
def get_weather(message):
    try:
        url = 'https://api.openweathermap.org/data/2.5/weather'
        params = {
            'appid': WEATHER_TOKEN,
            'q': message.text,
            'units': 'metric',
            'lang': 'ru',
        }
        response = requests.get(url, params=params)
        data = response.json()
        temp = (data['main']['temp'])
        conditions = (data['weather'][0]['description'])
        weather_message = f'В {message.text} сейчас {temp}, {conditions}'
        bot.send_message(message.chat.id, weather_message)
    except:
        bot.send_message(message.chat.id, f'{message.text} не желает контактировать с вами.'
                                          f' Возможно вы где-то ошиблись = (')


bot.polling(none_stop=True)

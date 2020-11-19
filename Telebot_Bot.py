import telebot
import requests
import os
from dotenv import load_dotenv
import time

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
WEATHER_TOKEN = os.getenv("WEATHER_TOKEN")

bot = telebot.TeleBot(token=TELEGRAM_TOKEN)
keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Какая погода за вашим окном?')


@bot.message_handler(commands=['help', 'Help'])
def help_text(message):
    user_help_text = '\n{0.first_name}, что такое области не знаю, соотвественно названия городов и сёл могу путать.' \
                     '\n\n\tДля получения информации просто напишите интересующий вас город.' \
                     '\n К примеру: Москва' \
                     '\n На текущий момент знаю команды:' \
                     '\n /start, /help'.format(message.from_user)
    bot.send_message(message.chat.id, user_help_text)


@bot.message_handler(commands=['start', 'Start', 'старт', 'Старт'])
def start_message(message):
    text_start_message = 'Привет {0.first_name}!, я {1.first_name}!\n Умею показывать погоду в одном' \
                         ' из существующих городов.'.format(message.from_user, bot.get_me())
    bot.send_message(message.chat.id, text_start_message, reply_markup=keyboard1)


@bot.message_handler(content_types=["text"])
def get_weather(message):
    try:
        # Getting data via the API.
        url = 'https://api.openweathermap.org/data/2.5/weather'
        params = {
            'appid': WEATHER_TOKEN,
            'q': message.text,
            'units': 'metric',
            'lang': 'ru',
        }
        response = requests.get(url, params=params)
        data = response.json()
        # Process data.
        get_weather_information(data, message)
    except:
        get_weather_except_message(message)


def get_weather_information(data, message):
    """
    Information to output to the request.
    :param data:
    :param message:
    :return:
    """
    temp = (data['main']['temp'])
    conditions = (data['weather'][0]['description'])
    weather_message = f'{message.text}: сейчас {temp}, {conditions}'
    bot.send_message(message.chat.id, weather_message)


def get_weather_except_message(message):
    """
    Error when entering the city incorrectly.
    :param message:
    :return:
    """
    bot.send_message(message.chat.id, f'{message.text} не желает контактировать с вами.'
                                      f' Возможно вы где-то ошиблись = (')


bot.polling(none_stop=True)

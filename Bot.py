import os

import time
import requests
from pprint import pprint

from dotenv import load_dotenv

load_dotenv()

WEATHER_TOKEN = os.getenv("WEATHER_TOKEN")


def get_weather():
    city_weather = input('Введите город для получания прогноза')
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city_weather,
        'appid': WEATHER_TOKEN,
    }
    response = requests.get(url, params=params).json()
    pprint(response)
    return response


get_weather()

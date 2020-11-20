import os

import time
import requests
from pprint import pprint

from dotenv import load_dotenv

load_dotenv()

WEATHER_TOKEN = os.getenv("WEATHER_TOKEN")


def get_weather():
    city_weather = input('Введите город для получения прогноза ')
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city_weather,
        'appid': WEATHER_TOKEN,
    }
    response = requests.get(url, params=params).json()
    # time_a = response['dt']
    # pprint(time_a)
    pprint(response)
    return response


def main():
    while True:
        try:
            get_weather()
            time.sleep(60*15)
        except Exception as e:
            print(f'Бот упал с ошибкой {e}')
            time.sleep(15)
            continue


# get_weather()

if __name__ == '__main__':
    main()
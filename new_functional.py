import telebot
import requests
import os
from dotenv import load_dotenv
import time


# Роутер команд. telebot

def route_command(command, message):
    if command == '/hello':
        pass


@bot.message_handler(content_types=["text"])
def main(message):
    while True:
        try:
            if message and message.text and message.text[0] == '/':
                print(f'Echo on "{message.text}"')
                route_command(message.text.lower(), message)
        except Exception as e:
            print(f'Бот упал с ошибкой: {e}')
            time.sleep(5)
            continue

# Добавить время для города из запроса выводить в сообщении о погоде.

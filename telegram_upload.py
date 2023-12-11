import telegram
import random
from os import listdir
import os
import time
from dotenv import load_dotenv


def post_photos(bot, sleep_timer, tg_chat_id):
    while True:
        folder_name = 'images'
        files = listdir(folder_name)
        random.shuffle(files)
        for file in files:
            with open(f'{folder_name}/{file}', 'rb') as photo:
                bot.send_photo(chat_id=tg_chat_id, photo=photo)
            time.sleep(sleep_timer)


def main():
    load_dotenv()
    tg_chat_id = os.environ['TG_CHAT_ID']
    token = os.environ['TELEGRAM_TOKEN']
    sleep_timer = 300
    bot = telegram.Bot(token=token)
    post_photos(bot, sleep_timer, tg_chat_id)


if __name__ == '__main__':
    main()
    
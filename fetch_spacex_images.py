import requests
import os
from download_image import download_image
import argparse


def fetch_spacex_last_launch(launch_id):
    url = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    response = requests.get(url)
    response.raise_for_status()
    response = response.json()['links']['flickr']['original']
    for photo_number, photo in enumerate(response):
         download_image(photo, f'images/spacex_{photo_number}.jpg')


def main():
    os.makedirs('images', exist_ok=True)
    description = 'эта программа позволяет скачать фото с spacex'
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument(
        '--launch_id',
        dest='launch_id',
        default='5eb87d47ffd86e000604b38a',
        help='введите id запуска'
    )
    args = parser.parse_args()
    fetch_spacex_last_launch(args.launch_id)
    

if __name__ == '__main__':
    main()
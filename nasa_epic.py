import os
import requests
from datetime import datetime
from download_image import download_image
from dotenv import load_dotenv


def get_nasa_epic(api_key):
    epic_url = 'https://api.nasa.gov/EPIC/api/natural/image'
    params = {'api_key' : api_key}
    response = requests.get(epic_url, params=params)
    response.raise_for_status()
    for epic_photo in response.json():
        image = epic_photo['image']
        date = epic_photo['date']
        date = datetime.fromisoformat(date).strftime("%Y/%m/%d")
        photo_url = f'https://api.nasa.gov/EPIC/archive/natural/{date}/png/{image}.png'
        download_image(photo_url, f'images/{image}.png', params)


def main():
    os.makedirs('images', exist_ok=True)
    load_dotenv()
    api_key = os.environ['NASA_API_KEY']
    get_nasa_epic(api_key)
    

if __name__ == '__main__':
    main()
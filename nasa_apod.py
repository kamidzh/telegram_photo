import requests
import os
from urllib.parse import unquote, urlparse
from download_image import download_image
from dotenv import load_dotenv


def get_file_extension(link):
    unquote_link = unquote(link)
    parse_link = urlparse(unquote_link)
    ext, fullname = os.path.split(parse_link.path)
    ext_file = os.path.splitext(fullname)
    filename, path = ext_file
    return print(path, filename)


def get_nasa_apod(api_key):
    url = 'https://api.nasa.gov/planetary/apod'
    count = 30 
    params = {
        'api_key' : api_key,
        'count' : count
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    images = []
    for nasa_apod in response.json():
        if nasa_apod.get('media_type') == 'image':
            if nasa_apod.get('hdurl'):
                images.append(nasa_apod.get('hdurl'))
            else:
                images.append(nasa_apod.get('url'))
    for photo_number, photo_url in enumerate(images):
         download_image(photo_url, f'images/nasa_apod_{photo_number}.jpg')


def main():
    os.makedirs('images', exist_ok=True)
    load_dotenv()
    api_key = os.environ['NASA_API_KEY']
    get_nasa_apod(api_key)
    

if __name__ == '__main__':
    main()
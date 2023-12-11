import requests
import os


def download_image(img_url, img_path, params=None):
    response = requests.get(img_url, params)
    response.raise_for_status()

    with open(img_path, 'wb') as file:
        file.write(response.content)



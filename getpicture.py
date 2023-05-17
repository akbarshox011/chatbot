import random

import requests


def getrandompicture():

    url = 'https://pixabay.com/api/?key=35656075-06406f3c7cda50868a13fd161&q=cats&image_type=photo'
    response = requests.get(url)

    data = response.json()
    links = []
    for item in data['hits']:
        link = item['pageURL']
        links.append(link)
    return random.choice(links)


import os
from datetime import datetime
import requests
from dotenv import load_dotenv
load_dotenv()


def getweatherinfo(cityname):
    try:
        url = 'https://api.openweathermap.org/data/2.5/weather'
        parametr = {
            'q': cityname,
            'appid': os.getenv('weatherapi'),
            'units': 'metric',
            'lang': 'ru'
        }

        response = requests.get(url, params=parametr)
        data = response.json()

        text = f"""Shahar nomi: {data['name']}
Ob-havo: {data['weather'][0]['main']}, {data['weather'][0]['description']}
Havo harorati: {data['main']['temp']} C˚
Tuyulishi: {data['main']['feels_like']} C˚
Eng past harorat: {data['main']['temp_min']} C˚
Eng yuqori harorat: {data['main']['temp_max']} C˚
Bosim: {data['main']['pressure']} P
Namlik:{data['main']['humidity']} %
Ko'ruvchanlik darajasi: {data['visibility']} m
Shamol tezligi: {data['wind']['speed']} m/s
Bulut: {data['clouds']['all']}
Mamalakat: {data['sys']['country']}
Quyosh chiqishi: {datetime.fromtimestamp(data['sys']['sunrise'])}
Quyosh botishi: {datetime.fromtimestamp(data['sys']['sunset'])}
Vaqt zonasi: {data['timezone']}
Shahar kodi: {data['cod']}
    """
        image = f"https://openweathermap.org/img/wn/{data['weather'][0]['icon']}@4x.png"
        return text, image

    except:
        return 'Shahar topilmadi'

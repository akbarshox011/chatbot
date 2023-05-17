import requests


def getconvertvalut(fromval, toval, amount):
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={toval}&from={fromval}&amount={amount}"

    payload = {}
    headers = {
        "apikey": "6037602865:AAE22XarbHaVTlyUem8HOsYgO0QesTE2sXI"
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    status_code = response.status_code
    result = response.json()

    return result
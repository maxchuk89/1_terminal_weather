import requests

WEATHER_URL = 'https://wttr.in/{}'

WEATHER_PARAMS = {
    'n': '',
    'q': '',
    'T': '',
    'M': '',
    'lang': 'ru',
}

OFFICE_NAMES = [
    'Лондон',
    'Шереметьево',
    'Череповец',
]


def get_weather(place):
    url = WEATHER_URL.format(place)
    response = requests.get(url, params=WEATHER_PARAMS)
    response.raise_for_status()
    return response.text


def main():
    for office in OFFICE_NAMES:
        print(get_weather(office))


if __name__ == '__main__':
    main()

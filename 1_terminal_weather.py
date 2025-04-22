import requests

WEATHER_URL  = 'https://wttr.in/{}?nqTM&lang=ru'
OFFICE_NAMES = [
    'Лондон',
    'Шереметьево',
    'Череповец'
]


def get_weather(place):
    response = requests.get(WEATHER_URL .format(place))
    response.raise_for_status()
    return response.text


def main():
    for office in OFFICE_NAMES:
        print(get_weather(office))


if __name__ == '__main__':
    main()

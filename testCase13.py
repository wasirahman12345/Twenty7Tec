#test case 13: Queries are getting performed successfully in Hindi language

import requests

from pprint import pprint

language = input('Enter your chosen language (hi for Hindi): ')

url = 'api.openweathermap.org/data/2.5/weather?APPID=9d50450a48809637b4862bdcb125927d&q=Paris,FR&units=metric&lang={}'.format(language)

res = requests.get(url)

data = res.json()

pprint (data)
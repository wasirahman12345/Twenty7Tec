# test case 11: Queries are getting performed successfully in French language

import requests

from pprint import pprint

language = input('Enter your chosen language (fr for French): ')

url = 'api.openweathermap.org/data/2.5/weather?APPID=9d50450a48809637b4862bdcb125927d&q=Paris,FR&units=metric&lang={}'.format(language)

res = requests.get(url)

data = res.json()

pprint (data)
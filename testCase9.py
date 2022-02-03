#test case 9: Queries are getting performed successfully for Tokyo,JP

import requests

from pprint import pprint

location = input('Enter your location (i.e. Tokyo,JP): ')

url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=9d50450a48809637b4862bdcb125927d&units=metric'.format(location)

res = requests.get(url)

data = res.json()

pprint (data)
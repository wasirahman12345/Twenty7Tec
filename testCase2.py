#test case 2: Queries are getting performed successfully for 2643743 (ID for London,GB)

import requests

from pprint import pprint

theId = input('Enter the ID for the location (i.e. 2643743): ')

url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=9d50450a48809637b4862bdcb125927d&units=metric'.format(location)

url = 'api.openweathermap.org/data/2.5/weather?APPID=9d50450a48809637b4862bdcb125927d&id=2643743&units=metric'

res = requests.get(url)

data = res.json()

pprint (data)
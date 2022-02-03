import requests

from pprint import pprint

theId = input('Enter the ID for the location (i.e. 421111): ')

url = 'http://api.openweathermap.org/data/2.5/weather?id={}&appid=9d50450a48809637b4862bdcb125927d&units=metric'.format(theId)

res = requests.get(url)

data = res.json()

pprint (data)
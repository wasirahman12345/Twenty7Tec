#test case 10: Queries are getting performed successfully for 1850147 (ID for Tokyo,JP)

import requests

from pprint import pprint

theId = input('Enter the ID for the location (i.e. 1850147): ')

url = 'http://api.openweathermap.org/data/2.5/weather?id={}&appid=9d50450a48809637b4862bdcb125927d&units=metric'.format(theId)

res = requests.get(url)

data = res.json()

pprint (data)
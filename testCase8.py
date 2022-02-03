#test case 8: Queries are getting performed successfully for 2650225 (ID for Delhi,IN)

import requests

from pprint import pprint

theId = input('Enter the ID for the location (i.e. 2650225): ')

url = 'http://api.openweathermap.org/data/2.5/weather?id={}&appid=9d50450a48809637b4862bdcb125927d&units=metric'.format(theId)

res = requests.get(url)

data = res.json()

pprint (data)
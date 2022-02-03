#test case 6: Queries are getting performed successfully for 5128581 (ID for New York,US)

import requests

from pprint import pprint

theId = input('Enter the ID for the location (i.e. 5128581): ')

url = 'http://api.openweathermap.org/data/2.5/weather?id={}&appid=9d50450a48809637b4862bdcb125927d&units=metric'.format(theId)

res = requests.get(url)

data = res.json()

pprint (data)
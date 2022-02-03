#test case 4: Queries are getting performed successfully for 2988507 (ID for Paris,FR)

import requests

from pprint import pprint

theId = input('Enter the ID for the location (i.e. 2988507): ')

url = 'http://api.openweathermap.org/data/2.5/weather?id={}&appid=9d50450a48809637b4862bdcb125927d&units=metric'.format(theId)

res = requests.get(url)

data = res.json()

pprint (data)
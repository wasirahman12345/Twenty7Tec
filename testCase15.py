#test case 15: Results from API are getting converted to Celsius

import requests

from pprint import pprint

weather = input ('Enter how you want to display temperature (metric for Celsius): ')

url = 'http://api.openweathermap.org/data/2.5/weather?q=London,GB&appid=9d50450a48809637b4862bdcb125927d&units={}'.format(weather)

res = requests.get(url)

data = res.json()

pprint (data)
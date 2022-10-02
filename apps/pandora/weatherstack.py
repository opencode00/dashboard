#c6bd0f699465c4142176361a6379a974
"http://api.weatherstack.com/current?access_key=c6bd0f699465c4142176361a6379a974&query=New York"

import requests

url = "http://api.weatherstack.com/current"
querystring = {"access_key":"c6bd0f699465c4142176361a6379a974", "query":"Santa Cruz de Tenerife"}
headers = {
    'cache-control': "no-cache"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
print(response.text)
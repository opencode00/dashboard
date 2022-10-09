
import requests

url = "https://opendata.aemet.es/opendata/api/prediccion/especifica/municipio/diaria/38038"

querystring = {"api_key":"eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJvcGVuY29kZTAwQGdtYWlsLmNvbSIsImp0aSI6IjJiNzUwZWNkLWZjNjktNDNkMi1iMmE2LWNjYTc0NTZlNmIwZCIsImlzcyI6IkFFTUVUIiwiaWF0IjoxNjYzNzAyMTEyLCJ1c2VySWQiOiIyYjc1MGVjZC1mYzY5LTQzZDItYjJhNi1jY2E3NDU2ZTZiMGQiLCJyb2xlIjoiIn0.qF5MU5jk5vy4ePoiCTej5MiQ3iL1-6_aKqAMMXTO5_k"}

headers = {
    'cache-control': "no-cache"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
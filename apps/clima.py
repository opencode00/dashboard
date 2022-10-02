from requests_html import HTMLSession
import requests

# url = 'https://www.el-tiempo.net/provincias/38/municipios/38038'

s = HTMLSession(verify=False)
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)'
    'AppleWebKit 537.36 (KHTML, like Gecko) Chrome',
    'Accept':'text/html,application/xhtml+xml,application/xml;'
    'q=0.9,image/webp,*/*;q=0.8'}


def eltiempo(mun):
    req = ''
    if mun == 'sc':
        req = 'https://www.eltiempo.es/santa-cruz-de-tenerife.html'
    if mun == 'll':
        req = 'https://www.eltiempo.es/san-cristobal-de-la-laguna.html'

    return eltiempo_tabla(req)  


def eltiempo_tabla(url):
    content = s.get(url, headers=headers)
    data = []
    fecha = content.html.find('h3')[1:]
    max = content.html.find('span.m_table_weather_day_max_temp')
    min = content.html.find('span.m_table_weather_day_min_temp')
    viento = content.html.find('span[data-wind]')
    clluvia = content.html.find('div.m_table_weather_day_rain')

    content = s.get(url+'?v=detallada', headers=headers)
    plluvia = content.html.find('i.icon-umbrella-blue~span')
    nube = content.html.find('i.icon-cloud-blue~span')
    luna = content.html.find('i.icon-moon-blue~span')

    for i in range(len(fecha)):
        data.append([fecha[i].text, 
            f'{max[i].text} - {min[i].text}', 
            viento[i].text.replace('km/h',""), 
            plluvia[i].text, 
            clluvia[i].text.replace('Lluvias',''), 
            nube[i].text,luna[i].text.replace('Ilum.',"")])
    
    return data

def eltiempo_informe():
    url = 'https://www.eltiempo.es/santa-cruz-de-tenerife.html'
    content = s.get(url, headers=headers)
    informe = content.html.find("span[data-route]", first=True)
    print(informe.attrs['data-route'])

def widgets(ciudad = 'sc'):
    q = 'Santa Cruz de Tenerife'
    if ciudad == 'll':
        q = 'San Cristobal de La Laguna,spain'
    url = "http://api.weatherstack.com/current"
    querystring = {"access_key":"c6bd0f699465c4142176361a6379a974", "query":q}
    headers = {
        'cache-control': "no-cache"
    }

    response = requests.request("GET", url, headers=headers, params=querystring).json()
    return f'''<img src="{response["current"]["weather_icons"][0]}"/><h3 style="display: inline;"> {response["current"]["weather_descriptions"][0]}</h3>'''
    

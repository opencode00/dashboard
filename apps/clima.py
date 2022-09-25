from requests_html import HTMLSession
import pprint

# url = 'https://www.el-tiempo.net/provincias/38/municipios/38038'

s = HTMLSession(verify=False)
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)'
    'AppleWebKit 537.36 (KHTML, like Gecko) Chrome',
    'Accept':'text/html,application/xhtml+xml,application/xml;'
    'q=0.9,image/webp,*/*;q=0.8'}


def el_tiempo():
    # temp = content.html.find('span.weather-today-now-current-temperature').text
    pass

def eltiempo(mun):
    req = ''
    if mun == 'sc':
        req = 'https://www.eltiempo.es/santa-cruz-de-tenerife.html'
    if mun == 'll':
        req = 'https://www.eltiempo.es/san-cristobal-de-la-laguna.html'

    return eltiempo_gen(req)  

def eltiempo_gen(url):
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

from requests_html import HTMLSession
import pprint

url = 'https://lagenda.org/programacion/planfinde'
s = HTMLSession(verify=False)
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)'
    'AppleWebKit 537.36 (KHTML, like Gecko) Chrome',
    'Accept':'text/html,application/xhtml+xml,application/xml;'
    'q=0.9,image/webp,*/*;q=0.8'}

def laagenda():
    titulos = []
    lugares = []
    data = []
    fdata = []
    sitios = []
    content = s.get(url, headers=headers)
    titulos = content.html.find('h4.title a')
    lugares = content.html.find('div.meta div:nth-child(3) a')
    
    for i in range(len(titulos)-1):
        ev = dict()
        ev['lugar'] = lugares[i].text
        ev['enlace'] = 'https://lagenda.org'+titulos[i].attrs["href"]
        ev['titulo'] = titulos[i].text
        sitios.append(lugares[i].text)
        data.append(ev)
    
    data.sort(key=lambda x: x['lugar'])
    sitios = list(set(sitios))
    sitios.sort()

    for i in sitios:
        lk = ''
        for j in range(len(titulos)-1):
            if (i == data[j]['lugar']):
                lk += f'<li><a href="{data[j]["enlace"]}" target=_blank>{data[j]["titulo"]}</a></li>'
        
        fdata.append(f'<h4>{i}</h4><ul>{lk}</ul>')
        
    pprint.pprint(fdata)
    return fdata


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
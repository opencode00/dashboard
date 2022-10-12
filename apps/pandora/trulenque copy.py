from requests_html import HTMLSession
from datetime import datetime
import pprint

s = HTMLSession(verify=False)
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)'
    'AppleWebKit 537.36 (KHTML, like Gecko) Chrome',
    'Accept':'text/html,application/xhtml+xml,application/xml;'
    'q=0.9,image/webp,*/*;q=0.8'}

def laagenda():
    url = 'https://lagenda.org/programacion/planfinde'
    titulos = []
    lugares = []
    data = []
    fdata = []
    sitios = []
    content = s.get(url, headers=headers)
    titulos = content.html.find('h4.title a')
    lugares = content.html.find('div.meta div:nth-child(3) a')
    fechas = content.html.find('div.post-date[itemprop=datePublished]') #178

    for i in range(len(titulos)-1):
        ev = dict()
        ev['lugar'] = lugares[i].text
        ev['enlace'] = 'https://lagenda.org'+titulos[i].attrs["href"]
        ev['titulo'] = titulos[i].text
        ev['fecha'] = fechas[i].text
        sitios.append(lugares[i].text)
        data.append(ev)
    
    data.sort(key=lambda x: x['lugar'])
    sitios = list(set(sitios))
    sitios.sort()

    for i in sitios:
        print(i)
    #     lk = ''
    #     for j in range(len(titulos)-1):
    #         if (i == data[j]['lugar']):
    #             lk += f'<li><a href="{data[j]["enlace"]}" target=_blank>{data[j]["fecha"]}{data[j]["titulo"]}</a></li>'
        
    #     fdata.append(f'<h4>{i}</h4><ul>{lk}</ul>')
        
    # # pprint.pprint(fdata)
    # return fdata

def cabtfe(url):
    content = s.get(url, headers=headers)
    titulos = content.html.find('h2 > a')
    data = []
    for i in titulos:
        data.append(f'<a href="httsp://www.tenerife.es{i.attrs["href"]}" target=_blank>{i.text}</a>')
    return data

def musica():
    h = datetime.now()
    url = 'https://www.tenerife.es/portalcabtfe/es/agenda?searchphrase=any&areas[]=flexicontent&filter_13[]=80&filter_245[]=2&filter_245[1]='+h.strftime('%Y-%m-%d')
    return cabtfe(url)

def expos():
    h = datetime.now()
    url = 'https://www.tenerife.es/portalcabtfe/es/agenda?searchphrase=any&areas[]=flexicontent&filter_13[]=78&filter_245[]=2&filter_245[1]='+h.strftime('%Y-%m-%d')
    return cabtfe(url)

def guimera():
    h = datetime.now()
    content = s.request('GET', f'https://teatroguimera.es/programacion-{h.strftime("%Y")}/', headers=headers, cookies={'uncode_privacy[consent_types]':'%5B%5D'})
    titulos = content.html.find('h3 > a')
    data = []
    for i in titulos:
        data.append(f'<a href="{i.attrs["href"]}" target=_blank>{i.text}</a>')
    return data   

def santiago_martin():
    content = s.get('https://pabellonsantiagomartin.net/eventos', headers=headers)
    titulos = content.html.find('h2 > a')
    data = []
    for i in titulos:
        data.append(f'<a href="https://pabellonsantiagomartin.net{i.attrs["href"]}" target=_blank>{i.text}</a>')
    return data

def rcnt():
    h = datetime.now()
    content = s.get('https://www.rcnt.es', headers=headers)
    fecha = content.html.find('div.ei-event')
    titulo = content.html.find('div.ei-name')
    desc = content.html.find('div.ei-description')
    image = content.html.find('div.ei-img')
    data = []
    for i in range(len(fecha)):
        f = datetime.strptime(fecha[i].attrs["data-start"], "%Y-%m-%d")
        if (h.month == f.month and h.year == f.year):
            # print(f'<a href="https://www.rcnt.es/{image[i].text}"><b>{fecha[i].attrs["data-start"]} - {titulo[i].text}</b></a>')
            data.append(f'<a href="https://www.rcnt.es/{image[i].text}" target=_blank><b>{f.day}/{f.month} - {titulo[i].text}</b></a>')

    return data

if __name__ == '__main__':
    pprint.pprint(laagenda())
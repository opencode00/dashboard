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
    content = s.get(url, headers=headers)
    titulos = content.html.find('h4.title a')
    lugares = content.html.find('div.meta div:nth-child(3) a')
    
    for i in range(len(titulos)-1):
        ev = dict()
        ev['lugar'] = lugares[i].text
        ev['enlace'] = 'https://laagenda.org'+titulos[i].attrs["href"]
        ev['titulo'] = titulos[i].text
        data.append(ev)
    
    data.sort(key=lambda x: x['lugar'])

    for i in range(len(data)):
        fdata.append(f'<h4>{data[i]["lugar"]}</h4><a href="{data[i]["titulo"]}" target=_blank>{data[i]["enlace"]}</a>')

    return fdata
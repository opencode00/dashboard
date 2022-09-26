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
        
    # pprint.pprint(fdata)
    return fdata
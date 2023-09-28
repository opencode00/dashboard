from requests_html import HTMLSession
from datetime import datetime
import pprint

s = HTMLSession(verify=False)
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)'
    'AppleWebKit 537.36 (KHTML, like Gecko) Chrome',
    'Accept':'text/html,application/xhtml+xml,application/xml;'
    'q=0.9,image/webp,*/*;q=0.8'}

sSC = ['Municipio de Santa Cruz','Santa Cruz','Auditorio de Tenerife Adán Martín','Biblioteca Municipal Central - TEA',
    'Espacio Cultural CajaCanarias Santa Cruz','Espacio La Granja','Museo Municipal de Bellas Artes de Santa Cruz','Museo de la Naturaleza y Arqueología',
    'Teatro Guimerá','TEA Tenerife Espacio de las Artes',"L'Incanto",'Asociación Cultural Equipo PARA','Café Teatro Rayuela',
    'Conservatorio Superior de Música de Canarias','Espacio Siglo XXI','Lanave de la Tribu']
sLL = ['La Laguna','Municipio de San Cristóbal de La Laguna','Valle Guerra','La Esperanza','Las Zocas','Aguere Espacio Cultural','Convento Santo Domingo La Laguna',
    'Aula Magna del Aulario de Guajara','Espacio Cultural CajaCanarias La Laguna','Paraninfo','Multicines Tenerife','Museo de la Ciencia y el Cosmos',
    'Casino de La Laguna','Casa Lercaro','Búho Club','Fundación Canaria Mapfre Guanarteme','Instituto Cabrera Pinto','La Bowie','Sala de Arte Bronzo',
    'Sala de Arte Paraninfo Pablo González de Vera','Vórtice Café']
sNORTE = ['Icod','El Tanque','La Matanza','La Orotava','San Juan de la Rambla','Santa Úrsula','Puerto de la Cruz','Vilaflor',
    'Espacio Cultural CajaCanarias Garachico','Espacio Cultural El Tanque','Teatro Cine Municipal Icod','Teatro El Sauzal','Recinto Festero']
sSUR = ['Tabaiba','Ecléctico Café','Güímar','Chío','San Miguel de Abona','Valle San Lorenzo','Guaza','Playa de Las Américas','Costa Adeje','Municipio de Guía de Isora',
    'Adeje Casco','Centro Cultural Los Cristianos','Auditorio Infanta Leonor','Casa de la Juventud de Adeje','La Casa Fuerte','Light Park Tenerife']

SC= []
LL = []
NORTE = []
SUR = []

def laagenda():
    url = 'https://lagenda.org/programacion/planfinde'
    titulos = []
    lugares = []
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

        if ev['lugar'] in sSC:
            html = f'<a href="{ev["enlace"]}" target=_blank>{ev["fecha"]} - {ev["titulo"]}</a>'
            SC.append(html)
        if ev['lugar'] in sLL:
            html = f'<a href="{ev["enlace"]}" target=_blank>{ev["fecha"]} - {ev["titulo"]}</a>'
            LL.append(html)
        if ev['lugar'] in sNORTE:
            html = f'<a href="{ev["enlace"]}" target=_blank>{ev["fecha"]} - {ev["titulo"]}</a>'
            NORTE.append(html)
        if ev['lugar'] in sSUR:
            html = f'<a href="{ev["enlace"]}" target=_blank>{ev["fecha"]} - {ev["titulo"]}</a>'
            SUR.append(html)
        
    return SC,LL,NORTE,SUR
    
def santa():
    url = 'https://www.elcorazondetenerife.com/agenda/'
    content = s.get(url, headers=headers)
    # titulos = content.html.find('span[itemprop=name]')
    # lugares = content.html.find('div.meta div:nth-child(3) a')
    # fechas = content.html.find('div.post-date[itemprop=datePublished]') #178
    return content.text


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
    pprint.pprint(santa())
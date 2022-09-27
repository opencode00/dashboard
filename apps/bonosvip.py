import requests as rq
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)'
           'AppleWebKit 537.36 (KHTML, like Gecko) Chrome',
           'Accept':'text/html,application/xhtml+xml,application/xml;'
           'q=0.9,image/webp,*/*;q=0.8'}

def close_sessions():
    rq.Session().close()
    rq.cookies.RequestsCookieJar().clear()

def get_bonosvip_empresa(item):
    return str(item.select_one('span.empresa').get_text()) + ' - ' + str(item.select_one('span.municipio').get_text())

def bonosvip(url):
    close_sessions()
    bvurl = 'http://www.bonosvip.com'
    
    #Obtenemos la cookie
    cookie = {'BVip18-e6b25e54455fd8ccfe775d94e18369f6' : rq.get(bvurl, headers = headers).cookies['BVip18-e6b25e54455fd8ccfe775d94e18369f6']}
    
    rawContent = rq.get(url, headers = headers, cookies = cookie).text
    
    bs = BeautifulSoup(rawContent, 'html.parser')
    rawItems = bs.find_all(class_ = 'bono')

    empresas = [get_bonosvip_empresa(item.select_one('div.localizacion')) for item in rawItems]
    enlaces = [item.select_one('a.bono-link')['href'] for item in rawItems]
    descripcion = [item.select_one('a.bono-link')['title'] for item in rawItems]
    precios = [item.select_one('span.price').get_text().strip() for item in rawItems]

    bonosvip = []
    for i in range(0,len(empresas)): 
        bonosvip.append(empresas[i] + '\n' + descripcion[i] + ' por ' + precios[i] + '\n ' + enlaces[i] + '\n\n')

    return bonosvip

def bonosvip_ocio():
    return bonosvip('https://bonosvip.com/23-ocio')
    
def bonosvip_restaurantes():
    return bonosvip('https://bonosvip.com/20-restaurantes')
    
def bonosvip_bienestar():
    return bonosvip('https://bonosvip.com/15-bienestar')
    
def bonosvip_hoteles():
    return bonosvip('https://bonosvip.com/16-hoteles')
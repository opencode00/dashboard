import requests as rq
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)'
           'AppleWebKit 537.36 (KHTML, like Gecko) Chrome',
           'Accept':'text/html,application/xhtml+xml,application/xml;'
           'q=0.9,image/webp,*/*;q=0.8'}


def gustazos():
    url = 'http://www.gustazos.com/SP_Tenerife'
    #con este bloque obtenemos el PHPSESSID
    with rq.Session() as s:
        r = s.get(url, headers = headers)
        #cookie = rq.utils.dict_from_cookiejar(s.cookies)['PHPSESSID']
    cookies = rq.utils.dict_from_cookiejar(s.cookies)
    content = rq.get(url, headers = headers, cookies = cookies).text

    #crea objeto beautifulsoup
    bs = BeautifulSoup(content, 'html.parser')
    #Obtiene listado de las divs con clase coupon-list__row
    rawItems = bs.find_all('div', attrs={'class': 'name coupon-list-item__footer__name'})

    #list comprehencion
    empresas = [item.select_one('p.coupon-list-item__footer__name__title > a').get_text().strip() for item in rawItems]
    enlaces = [item.select_one('p.coupon-list-item__footer__name__title > a')['href'] for item in rawItems]
    descripcion = [item.select_one('span.tooltop').get_text() for item in rawItems]

    gustazos = []
    for i in range(0,len(empresas)): 
        gustazos.append(empresas[i] + '\n' + descripcion[i] + '\n ' + 'http://www.gustazos.com/' + enlaces[i] + '\n\n')

    return gustazos
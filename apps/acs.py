import requests as rq
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)'
           'AppleWebKit 537.36 (KHTML, like Gecko) Chrome',
           'Accept':'text/html,application/xhtml+xml,application/xml;'
           'q=0.9,image/webp,*/*;q=0.8'}

def acs():
    url = 'http://www.gobiernodecanarias.org/academia/scripts/default.asp'
    content = rq.get(url, headers = headers).text
    
    bs = BeautifulSoup(content, 'html.parser')
    rawItems = bs.find ('div', {'id' : 'country2'}) 
    items = rawItems.find_all('td')
    cursos = ""
    lista = []
    for i in range(len(items)-1, 0, -1):
        if (i > 2) and ('Tenerife' in str(items[i])):
            cursos = str(items[i-2].get_text()) + "\n"
            cursos += "http://www.gobiernodecanarias.org/academia/scripts/" + str(items[i-2].a['href']) + "\n\n"
            lista.append(cursos)
    return lista
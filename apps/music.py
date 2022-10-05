#https://myradioonline.es/los40-classic/listas
#https://myradioonline.es/kiss-fm/listas
    #div.plist-item (enlace youtube)
    #div.plist-item span[itemprop] (artista - cancion)

#https://www.hitfm.es/hit-30/
    # titulo:  h2.entry-title
    # artista: h3
    #enlce: div.youtube img 

#Ha sonado ('div.ha-sonado div.data div.titulo|artista')
# https://play.los40.com/emisora/los40_classic/
# https://play.los40.com/
# https://play.los40.com/emisora/los40_catalunya/

from requests_html import HTMLSession
from selenium.webdriver  import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import pprint as p

s = HTMLSession(verify=False)
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)'
    'AppleWebKit 537.36 (KHTML, like Gecko) Chrome',
    'Accept':'text/html,application/xhtml+xml,application/xml;'
    'q=0.9,image/webp,*/*;q=0.8'}

def los40():
    url = 'https://los40.com/lista40/'
    lista = []
    content = s.get(url, headers=headers)
    lista40 = content.html.find('div[data-url_youtube]')
    
    for i in lista40:
        item = f'{i.attrs["data-titulo_cancion"]} <br> {i.attrs["data-nombre_artista"]} <br> <a href="{i.attrs["data-url_media"]}">Oir</a> <a href="{i.attrs["data-url_youtube"]}">YT</a>'
        lista.append(item)
    return lista

def hitfm():
    url = 'https://www.hitfm.es/hit-30/'
    opts = Options()
    opts.add_argument('--headless')
    driver = Chrome(executable_path='d:\\work\\dashboard\\chromedriver.exe', options=opts)
    driver.get(url)
    titulos = driver.find_elements(By.CSS_SELECTOR, 'h2.entry-title')
    artistas = driver.find_elements(By.CSS_SELECTOR, 'h3')
    enlaces = driver.find_elements(By.CSS_SELECTOR, '.youtube img')
    muestra = driver.find_elements(By.CSS_SELECTOR, 'source')
    data = []

    for i in range(len(enlaces)):
        img = enlaces[i].get_attribute('src')
        img = img.replace('https://img.youtube.com/vi/','')
        # print(img[:-6])
        data.append(f'{titulos[i].text} <br> {artistas[i].text} <br> <a href="https://www.youtube.com/watch?v={img[:-6]}" target=_blank> YT </a> <a href="{muestra[i].get_attribute("src")}" target=_blank> Muestra </a>')

    return data


p.pprint(hitfm())
from requests_html import HTMLSession
import pprint as p
#https://myradioonline.es/los40-classic/listas
#https://myradioonline.es/kiss-fm/listas
    #div.plist-item (enlace youtube)
    #div.plist-item span[itemprop] (artista - cancion)

#Ha sonado ('div.ha-sonado div.data div.titulo|artista')
# https://play.los40.com/emisora/los40_classic/
# https://play.los40.com/
# https://play.los40.com/emisora/los40_catalunya/

#https://www.hitfm.es/hit-30/
    # titulo:  h2.entry-title
    # artista: h3
    #enlce: div.youtube img 

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
        item = f'{i.attrs["data-nombre_artista"]} <br> {i.attrs["data-titulo_cancion"]} <br> <a href="{i.attrs["data-url_media"]}">Oir</a> <a href="{i.attrs["data-url_youtube"]}">YT</a>'
        lista.append(item)
    return lista


# p.pprint(los40())
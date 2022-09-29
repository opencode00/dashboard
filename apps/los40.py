from requests_html import HTMLSession
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
        item = f'{i.attrs["data-nombre_artista"]} <br> {i.attrs["data-titulo_cancion"]} <br> <a href="{i.attrs["data-url_media"]}">Oir</a> <a href="{i.attrs["data-url_youtube"]}">YT</a>'
        lista.append(item)
    return lista


# p.pprint(los40())
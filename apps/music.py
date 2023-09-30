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
import re

import pprint as p

s = HTMLSession(verify=False)
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)'
    'AppleWebKit 537.36 (KHTML, like Gecko) Chrome',
    'Accept':'text/html,application/xhtml+xml,application/xml;'
    'q=0.9,image/webp,*/*;q=0.8'}

def item(titulo, artista, enlaceyt, enlace=None):
    if enlace is not None:
        return f'<b>{titulo}</b> <br> {artista} <br> <a href="{enlaceyt}" target=_blank> YT </a> <a href="{enlace}" target=_blank> Muestra </a>'
    
    return f'<b>{titulo}</b> <br> {artista} <br> <a href="{enlaceyt}" target=_blank> YT </a>'

def los40():
    url = 'https://los40.com/lista40/'
    lista = []
    content = s.get(url, headers=headers)
    # return content.html.absolute_links
    # exit()
    items = content.html.find('ul.lst-can li')

    for item in items:
        if 'id' in item.attrs:
            artist = item.find('div.c-ele div p span', first=True).text
            title = item.find('div.c-ele div p', first=True).text.replace(artist, "")
            audios= item.find('ul.l-esc li a')
            for audio in audios:
                preview = ''
                if 'href' in audio.attrs:
                    if 'https://music.apple.con' not in audio.attrs['href']:
                        preview = audio.attrs['href'] 
            yts = item.find('iframe', first=True)
            yt = ''
            if yts is not None:
                yt = 'https://www.youtube.com/watch?v='+yts.attrs['src'].replace('https://www.youtube.com/embed/', "")
            print(f'{title} - {artist} - {preview} - {yt}')
            # lista.append(item(i.attrs["title"], "", i.attrs["src"]))
            
    # return lista

def hitfm2():
    url = 'https://www.hitfm.es/hit-30/'
    content = s.get(url, headers=headers)
    data = []
    muestras = re.findall('<source src=\"(.+.mp3)', content.text)
    enlaces = re.findall('\[meta_value\] \=\> https\:\/\/www.youtube.com\/watch\?v\=(.+)\n', content.text)
    artistas = re.findall('<h3>(.+)</h3>', content.text)
    titulos = re.findall('-->\n(.+)<\/h2>', content.text)
    
    for i in range(len(enlaces)):
        data.append(item(titulos[i].strip(), artistas[i], 'https://www.youtube.com/watch?v='+enlaces[i], muestras[i]))

    return data

def myradioonline(emisora=None):
    url = 'https://myradioonline.es/los40-classic/listas'
    if emisora == 'kiss':
        url = 'https://myradioonline.es/kiss-fm/listas'
    
    data = []
    content = s.get(url, headers=headers)
    titulos = content.html.find('span[itemprop=name]')[4:]
    artista = content.html.find('span[itemprop=byArtist]')[1:]
    enlace = content.html.find('div.plist-item')[1:]

    for i in range(len(titulos)):
        # print(titulos[i].text, artista[i].text, enlace[i].attrs['data-youtube'])
        data.append(item(titulos[i].text, artista[i].text, 'https://www.youtube.com/watch?v='+enlace[i].attrs['data-youtube']))
    
    return data

if __name__ == "__main__":
    p.pprint(los40())
    # p.pprint(myradioonline())
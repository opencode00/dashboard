from requests_html import HTMLSession
import pprint

# url = 'https://www.el-tiempo.net/provincias/38/municipios/38038'
url = 'https://www.eltiempo.es/santa-cruz-de-tenerife.html'
s = HTMLSession(verify=False)
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)'
    'AppleWebKit 537.36 (KHTML, like Gecko) Chrome',
    'Accept':'text/html,application/xhtml+xml,application/xml;'
    'q=0.9,image/webp,*/*;q=0.8'}


def el_tiempo():
    # temp = content.html.find('span.weather-today-now-current-temperature').text
    pass

def eltiempo():
    content = s.get(url, headers=headers)
    temp = content.html.find('.c-tib-text')
    print(content.text)

eltiempo()
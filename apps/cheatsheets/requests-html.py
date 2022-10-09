from requests_html import HTMLSession

s = HTMLSession(verify=False)
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)'
    'AppleWebKit 537.36 (KHTML, like Gecko) Chrome',
    'Accept':'text/html,application/xhtml+xml,application/xml;'
    'q=0.9,image/webp,*/*;q=0.8'}

def laagenda():
    url = 'https://lagenda.org/programacion/planfinde'
    content = s.get(url, headers=headers)

    titulos = []
    lugares = []
    titulos = content.html.find('h4.title a')
    lugares = content.html.find('div.meta div:nth-child(3) a')

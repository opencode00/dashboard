from requests_html import HTMLSession

s = HTMLSession(verify=False)
url = 'https://yelmocines.es/now-playing.aspx/GetNowPlaying'

headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)'
    'AppleWebKit 537.36 (KHTML, like Gecko) Chrome',
    'Accept':'text/html,application/xhtml+xml,application/xml;'
    'q=0.9,image/webp,*/*;q=0.8'}

def yelmo():
    content = s.post(url,{'cityKey': 'santa-cruz-tenerife'})
    print (content.text)

yelmo()


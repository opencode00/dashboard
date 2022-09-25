from requests_html import HTMLSession
import pprint

url = 'https://api.themoviedb.org/3/movie/550?api_key=118d0e0aadde8ef816e4f0e8f19fc468'
s = HTMLSession(verify=False)
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)'
    'AppleWebKit 537.36 (KHTML, like Gecko) Chrome',
    'Accept':'text/html,application/xhtml+xml,application/xml;'
    'q=0.9,image/webp,*/*;q=0.8'}

    

    
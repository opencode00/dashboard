#https://www.justwatch.com/es

# https://www.themoviedb.org/?language=es (API_KEY:118d0e0aadde8ef816e4f0e8f19fc468)

import requests as rq
from requests_html import HTMLSession
import pprint as p

s = HTMLSession(verify=False)
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome',
    'Accept': 'application/json',
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxMThkMGUwYWFkZGU4ZWY4MTZlNGYwZThmMTlmYzQ2OCIsInN1YiI6IjU4OTIxNGUzOTI1MTQxMmRkNzAwOTY5YSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.fm7GExZr-T2lf-LKRlO2hwSChnANjLjnDpTsgqykgTM',
    # 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxMThkMGUwYWFkZGU4ZWY4MTZlNGYwZThmMTlmYzQ2OCIsInN1YiI6IjU4OTIxNGUzOTI1MTQxMmRkNzAwOTY5YSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.fm7GExZr-T2lf-LKRlO2hwSChnANjLjnDpTsgqykgTM',
    #'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
    }

headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)''AppleWebKit 537.36 (KHTML, like Gecko) Chrome',
           'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}

def req(type):
    api_key = '118d0e0aadde8ef816e4f0e8f19fc468'
    cmds = {'series_p': 'trending/tv/day', 'pelis_p': 'trending/movie/day' }
    opts = 'language=es-ES'
    # print(f'https://api.themoviedb.org/3/{cmds[type]}?api_key={api_key}&{opts}')
    return f'https://api.themoviedb.org/3/{cmds[type]}?api_key={api_key}&{opts}'

def formatData(data, type):
    if type=='tv':
        return f"<td width=25%><a href=\"https://www.themoviedb.org/{type}/{data['id']}-{data['original_name'].replace(' ','-')}?language=es\" target=_blank><img src='https://image.tmdb.org/t/p/w200{data['poster_path']}'></a></td><td><ul><li>{data['name']}</li><li>{data['vote_average']}</li><li>{data['overview']}</li></ul></td>"
    else:
        return f"<td width=25%><a href=\"https://www.themoviedb.org/{type}/{data['id']}-{data['original_title'].replace(' ','-')}?language=es\" target=_blank><img src='https://image.tmdb.org/t/p/w200{data['poster_path']}'></a></td><td><ul><li>{data['title']}</li><li>{data['vote_average']}</li><li>{data['overview']}</li></ul></td>"


def populars(type, subtype):
    items = []
    r = rq.get(req(type), headers=headers).json()

    for i in r['results']:
        items.append(formatData(i,subtype))

    return items

def justwatch():
    content = s.get('https://www.justwatch.com/es', headers=headers)
    # return content.text
    data = []
    enlaces = content.html.find('a.title-list-grid__item--link')
    images = content.html.find('img.picture-comp__img')
    
    for i in range(len(enlaces)):
        src = images[i].attrs['src']
        if 'data-src' in images[i].attrs:
            src = images[i].attrs['data-src']
        data.append(f'<a href="https://justwatch.com{enlaces[i].attrs["href"]}" target=_blank> <img src="{src}" alt="{images[i].attrs["alt"]}"></a>')
    
    return data

if __name__ == '__main__':
    # print(justwatch().encode('utf-8'))
    p.pprint(justwatch())

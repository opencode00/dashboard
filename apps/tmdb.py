import requests as rq
import pprint

headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)'
    'AppleWebKit 537.36 (KHTML, like Gecko) Chrome',
    'Accept':'text/html,application/xhtml+xml,application/xml;'
    'q=0.9,image/webp,*/*;q=0.8'}

def req(type):
    api_key = '118d0e0aadde8ef816e4f0e8f19fc468'
    cmds = {'series_p': 'tv/popular', 'pelis_p': 'movie/popular' }
    opts = 'language=es-ES'
    # print(f'https://api.themoviedb.org/3/{cmds[type]}?api_key={api_key}&{opts}')
    return f'https://api.themoviedb.org/3/{cmds[type]}?api_key={api_key}&{opts}'

def populars():
    series = rq.get(req('series_p'), headers=headers).json()
    # pelis = s.get(req('pelis_p'), headers=headers) .jsso
    # pprint.pprint(series['results'][0]['name'])
    print(len(series['results']) )
    #https://image.tmdb.org/t/p/w500/kqjL17yufvn9OVLyXYpvtyrFfak.jpg
    #id, name, original_name, overview (), vote_average, https://image.tmdb.org/t/p/w500+poster_path, enlace: https://www.themoviedb.org/tv/id-original-name?language=es

populars()
    
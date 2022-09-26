import requests as rq

headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)''AppleWebKit 537.36 (KHTML, like Gecko) Chrome',
           'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}

def req(type):
    api_key = '118d0e0aadde8ef816e4f0e8f19fc468'
    cmds = {'series_p': 'tv/popular', 'pelis_p': 'movie/popular' }
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
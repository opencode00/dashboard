mtopbar = [
    {'title':'Files','url':'./files', 'icon':'folder_open'},
    {'title':'Music','url':'http://flix.port0.org', 'icon':'music_note'},
    {'title':'Music','url':'http://opencode.port0.org/music', 'icon':'play_arrow'},
    {'title':'Terminal','url':'https://dox.port0.org', 'icon':'terminal'},
]

def topbar():
    out = []
    for i in mtopbar:
        out.append(f'''
        <li class="dropdown">
            <a target=_blank href="{i['url']}">
                <span style="font-size:45px" class="material-symbols-rounded text2middle">{i['icon']}</span>
                <span class="d-lg-none d-md-block">{i['title']}</span>
            </a>
        </li>
        ''')
    return out
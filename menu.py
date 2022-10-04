menu = [
    {'title':'Clima','url':'./clima', 'icon':'weather_snowy'},
    {'title':'Trulenque','url':'./trulenque', 'icon':'celebration'},
    {'title':'Música','url':'./listen', 'icon':'play_circle'},
    {'title':'Cine','url':'./cine', 'icon':'play_circle'},
    {'title':'Que ver','url':'./quever', 'icon':'movie'},
    {'title':'Cupones','url':'./cupones', 'icon':'savings'},
    {'title':'Cursos','url':'./cursos', 'icon':'draw'},
]

def build_menu(req):
    out = []
    for i in menu:
        clase = ''
        if f".{req}" == i['url']:
            clase = ' class="active" '
        out.append(f'''
            <li{clase}>
                <a href="{i['url']}">
                    <span class="material-symbols-rounded text2middle">{i['icon']}</span>
                    <span>{i['title']}</span>
                </a>
            </li>
        ''')
    return out
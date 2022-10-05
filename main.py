from flask import Flask, render_template, request
import menu, topbar
from apps import music, trulenque, clima, tmdb, yelmo

app = Flask(__name__)

@app.get('/')
def index():
    return render_template("index.html", 
        bTopbar = topbar.topbar(),
        menu = menu.build_menu(request.path),
    )

@app.get('/clima')
def tiempo():
    return render_template("clima.html", 
        bTopbar = topbar.topbar(),
        menu = menu.build_menu(request.path),
        sc = clima.tiempo('sc'), 
        ll= clima.tiempo('ll'), 
    )

@app.get('/trulenque')
def fogalera():
    return render_template("trulenque.html", 
        bTopbar = topbar.topbar(),
        menu = menu.build_menu(request.path),
        eventos = trulenque.laagenda(), 
    )

@app.get('/listen')
def listen():
    return render_template("music.html", 
        bTopbar = topbar.topbar(),
        menu = menu.build_menu(request.path),
        ppales = music.los40(),
        hitfm = music.hitfm(),

    )

@app.get('/cine')
def cine():
    pass
    return render_template("cine.html", 
        bTopbar = topbar.topbar(),
        menu = menu.build_menu(request.path),
        # meridiano = yelmo.cines('meridiano'),
        # orotava = yelmo.cines('orotava'),
    )

@app.get('/quever')
def quever():
    return render_template("quever.html", 
        bTopbar = topbar.topbar(),
        menu = menu.build_menu(request.path),
        series = tmdb.populars('series_p', 'tv'), 
        pelis = tmdb.populars('pelis_p', 'movies'),
    )

@app.get('/cupones')
def cupones():
    pass
    return render_template("index.html", 
        bTopbar = topbar.topbar(),
        menu = menu.build_menu(request.path),
    )

@app.get('/cursos')
def cursos():
    pass
    return render_template("index.html", 
        bTopbar = topbar.topbar(),
        menu = menu.build_menu(request.path),
    )


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
from flask import Flask, render_template, request
import menu, topbar
from apps import trulenque, clima, tmdb, los40, yelmo

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
        widgetsc = clima.widgets('sc'),
        widgetll = clima.widgets('ll'),
        bTopbar = topbar.topbar(),
        menu = menu.build_menu(request.path),
        sc = clima.eltiempo('sc'), 
        ll= clima.eltiempo('ll'), 
    )

@app.get('/trulenque')
def fogalera():
    return render_template("trulenque.html", 
        bTopbar = topbar.topbar(),
        menu = menu.build_menu(request.path),
        eventos = trulenque.laagenda(), 
    )

@app.get('/media')
def media():
    return render_template("entertainement.html", 
        bTopbar = topbar.topbar(),
        menu = menu.build_menu(request.path),
        ppales = los40.los40(),
        meridiano = yelmo.cines('meridiano'),
        orotava = yelmo.cines('orotava'),
    )

@app.get('/quever')
def quever():
    return render_template("quever.html", 
        bTopbar = topbar.topbar(),
        menu = menu.build_menu(request.path),
        series = tmdb.populars('series_p', 'tv'), 
        pelis = tmdb.populars('pelis_p', 'movies'),
    )

# @app.get('/cursos')
# def cursos():
#     return render_template("index.html", 
#         bTopbar = topbar.topbar(),
#         menu = menu.build_menu(request.path),
#         sc = clima.eltiempo('sc'), 
#         ll= clima.eltiempo('ll'), 
#     )


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
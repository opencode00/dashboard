from doctest import REPORTING_FLAGS
from flask import Flask, render_template, request, make_response
import menu, topbar
from apps import music, trulenque, clima, tmdb, yelmo, gustazos, bonosvip, cursos

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
        moon = clima.getTodayMoon(), 
        moons = clima.getMonthMoons(),
        calmoon = clima.getCalendarMoons()
    )

@app.get('/trulenque')
def fogalera():
    return render_template("trulenque.html", 
        bTopbar = topbar.topbar(),
        menu = menu.build_menu(request.path),
        laagenda = trulenque.laagenda(), 
        musica = trulenque.musica(), 
        expos = trulenque.expos(), 
        guimera = trulenque.guimera(), 
        smartin = trulenque.santiago_martin(), 
        rcnt = trulenque.rcnt(), 

    )

@app.get('/listen')
def listen():
    response = make_response(render_template("music.html", 
        bTopbar = topbar.topbar(),
        menu = menu.build_menu(request.path),
        ppales = music.los40(),
        hitfm = music.hitfm2(),
        radiosonline = '<a href="https://myradioonline.es/" target=_blank> Radios online </a>',
        # kiss = '<a href="https://myradioonline.es/kiss-fm/listas" target=_blank> Kiss FM </a>',
        # classics = '<a href="https://myradioonline.es/los40-classic/listas" target=_blank> Los 40 Classic </a>',
        kiss = music.myradioonline('kiss'),
        classics = music.myradioonline('classics'),
    ))
    response.headers["Cache-Control"] = "public Max-age=86400" 
    return response

@app.get('/cine')
def cine():
    pass
    return render_template("cine.html", 
        bTopbar = topbar.topbar(),
        menu = menu.build_menu(request.path),
        meridiano = yelmo.cines()[0],
        orotava = yelmo.cines()[1],
    )

@app.get('/quever')
def quever():
    return render_template("quever.html", 
        bTopbar = topbar.topbar(),
        menu = menu.build_menu(request.path),
        series = tmdb.populars('series_p', 'tv'), 
        pelis = tmdb.populars('pelis_p', 'movies'),
        justwatch = tmdb.justwatch(),
    )

@app.get('/cupones')
def cupones():
    pass
    return render_template("cupones.html", 
        bTopbar = topbar.topbar(),
        menu = menu.build_menu(request.path),
        gustazos = gustazos.gustazos(),
        bonosRest =  bonosvip.bonosvip_restaurantes(),
        bonosOcio =  bonosvip.bonosvip_ocio(),
        bonosHotel =  bonosvip.bonosvip_hoteles(),
        # bonoBien =  bonosvip.bonosvip_bienestar(),
    )

@app.get('/cursos')
def learn():
    pass
    return render_template("cursos.html", 
        bTopbar = topbar.topbar(),
        menu = menu.build_menu(request.path),
        cursos = cursos.acs(),
    )


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
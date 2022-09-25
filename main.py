from flask import Flask, render_template
from apps import trulenque
from apps import clima
from apps import tmdb

app = Flask(__name__)

@app.get('/')
def index():
    return render_template("index.html", 
        sc = clima.eltiempo('sc'), 
        ll= clima.eltiempo('ll'), 
        eventos = trulenque.laagenda(), 
        series = tmdb.populars('series_p', 'tv'), 
        pelis = tmdb.populars('pelis_p', 'movies'))

@app.get('/test')
def test():
    return render_template("dashboard.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
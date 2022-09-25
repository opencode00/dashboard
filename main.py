from flask import Flask, render_template
from apps import apps

app = Flask(__name__)

@app.get('/')
def index():
    return render_template("index.html", sc = apps.eltiempo('sc'), ll= apps.eltiempo('ll'), eventos = apps.laagenda())

@app.get('/test')
def test():
    return render_template("dashboard.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
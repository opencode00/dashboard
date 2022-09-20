from flask import Flask, render_template
from apps.peppapig import common, get_last

app = Flask(__name__)

@app.get('/')
def index():
    pepa = get_last.euro_last(get_last.last('EMIL'))
    print(pepa[0])
    return render_template("index.html", euro  = str(pepa[0]))

@app.get('/test')
def test():
    return render_template("dashboard.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
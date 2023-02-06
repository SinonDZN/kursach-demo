from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/main')
def hello_world():
    return render_template("index.html")


@app.route('/katalog')
def katalog():
    return render_template("katalog.html")


@app.route('/info')
def info():
    return render_template("info.html")


@app.route('/cart')
def cart():
    return 'Корзина'


@app.route('/iphone14promax')
def iphone14promax():
    return render_template("iphone14promax.html")


if __name__ == '__main__':
    app.run(debug=True)

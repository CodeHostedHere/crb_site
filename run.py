from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/tos')
def index():
    return render_template('tos.html')


@app.route('/privacy')
def index():
    return render_template('privacy.html')
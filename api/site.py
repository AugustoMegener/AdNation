from api.data import getData
from flask import Flask, render_template

site = Flask('AdNation')


@site.route('/')
def home():
    return render_template('home.html', **getData())


def run(): 
    site.run(host='0.0.0.0', port=8080, debug=True)
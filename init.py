from flask import Flask, render_template
from json import loads

config = (loads(open('config.json', 'r').read()) |
          {'content': open('site_content.md', 'r').read().strip()})
site = Flask('AdNation')


@site.route('/')
def home():
    return render_template('home.html', **config)


site.run(debug=True)

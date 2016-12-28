from flask import render_template
import requests

from app import app


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/pi')
def pi():
    r = requests.get(app.config['PI_HOST'] + '/ping',
                     auth=(app.config['PI_USER'], app.config['PI_PASSWORD']))
    print r.status_code
    return r.text, r.status_code

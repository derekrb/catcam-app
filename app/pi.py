import requests

from app import app


AUTH = (app.config['PI_USER'], app.config['PI_PASSWORD'])


def get(path, **params):
    url = app.config['PI_HOST'] + path
    return requests.get(url, auth=AUTH, params=params)

import requests

from app import app


AUTH = (app.config['PI_USER'], app.config['PI_PASSWORD'])


def make_url(path):
    return app.config['PI_HOST'] + path


def get(path, stream=False, **params):
    return requests.get(make_url(path), auth=AUTH, params=params, stream=stream)

import flask_wtf
from wtforms import SubmitField


class TestVideo(flask_wtf.FlaskForm):
    submit = SubmitField('Play Video')

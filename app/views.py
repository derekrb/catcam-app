from flask import render_template, Response, stream_with_context

from app import app
import forms
import pi


@app.route('/', methods=['GET', 'POST'])
def index():

    form = forms.TestVideo()
    if form.validate_on_submit():
        pi.get('/video', video='test')

    return render_template('index.html', form=form)


@app.route('/pi')
def ping():
    r = pi.get('/ping')
    return r.text, r.status_code


@app.route('/stream')
def stream():
    r = pi.get('/stream', stream=True)
    return Response(stream_with_context(r.iter_content(1024)),
                    content_type=r.headers['content-type'])

from flask import Flask, render_template, request, send_file
from werkzeug.middleware.proxy_fix import ProxyFix
import requests
import os

app = Flask(__name__)
app.config['DEBUG'] = False
TEMPLATES_AUTO_RELOAD = True

app.wsgi_app = ProxyFix(
    app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/download-resume')
def send_download():
    filename = 'Sahas_Makhadhevan_Resume.pdf'
    return send_file(os.path.join('downloads', filename), as_attachment=True)


@app.route('/experiences')
def experiences():
    return render_template('experiences.html')


@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')


if __name__ == '__main__':
    app.run()

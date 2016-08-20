import os

from flask import Flask, render_template, request
import hanja


__version__ = '0.1.0'


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/translate')
def translate():
    text = request.args['t']
    result = hanja.translate(text, 'substitute')

    return result


if __name__ == '__main__':
    # application = create_app()
    application = app
    host = os.environ.get('HOST', '0.0.0.0')
    port = int(os.environ.get('PORT', 8016))
    debug = bool(os.environ.get('DEBUG', False))

    application.run(host=host, port=port, debug=debug)

import flask

app = flask.Flask(__name__)


@app.route('/')
def index():
    return flask.render_template('index.html')


@app.route('/about_project')
def about_project():
    return flask.render_template('about_project.html')


@app.route('/close')
def close():
    return 'close'


@app.route('/establish')
def establish():
    return 'establish'


@app.route('/alive')
def alive():
    return 'alive'


@app.route('/water')
def water():
    return 'water'


@app.route('/storm')
def storm():
    return 'storm'


if __name__ == '__main__':
    app.run(host='0.0.0.0')

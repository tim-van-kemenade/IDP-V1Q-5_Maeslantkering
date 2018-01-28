import flask
import urllib.request as request

app = flask.Flask(__name__)


@app.route('/')
def index():
    return flask.render_template('index.html')


@app.route('/about_project')
def about_project():
    return flask.render_template('about_project.html')


@app.route('/wind_json')
def wind_json():
    json_url = 'url'  # TODO: insert url from which the server hosts json as string
    with request.urlopen(json_url) as url:
        json_data = url.read().decode()  # TODO: ensure that json_data format is correct JSON so it can get passed on
    return json_data


@app.route('/close')
def close():
    return 'close'  # TODO: SNE place some of your stuff here


@app.route('/establish')
def establish():
    return 'establish'  # TODO: SNE place some of your stuff here


@app.route('/alive')
def alive():
    return 'alive'  # TODO: SNE place some of your stuff here


@app.route('/water')
def water():
    return 'water'  # TODO: SNE place some of your stuff here


@app.route('/storm')
def storm():
    return 'storm'  # TODO: SNE place some of your stuff here


if __name__ == '__main__':
    app.run(host='0.0.0.0')

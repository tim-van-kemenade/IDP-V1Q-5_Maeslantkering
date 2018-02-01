import flask

app = flask.Flask(__name__)


@app.route('/')
def index():
    return flask.render_template('index.html')


@app.route('/about_project')
def about_project():
    return flask.render_template('about_project.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')

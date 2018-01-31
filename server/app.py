from flask import Flask, Response
from flask_cors import CORS


class App:
    app = None

    def __init__(self):
        self.app = Flask(__name__)
        CORS(self.app)

    def run(self):
        self.app.run(port=1337, host='192.168.42.1')

    def register_controller(self, controller):
        controller.add_routes(self)

    def add_endpoint(self, endpoint=None, endpoint_name=None, handler=None):
        self.app.add_url_rule(endpoint, endpoint_name, EndpointAction(handler))


class EndpointAction(object):
    def __init__(self, action):
        self.action = action
        self.response = Response(status=200, headers={})

    def __call__(self, *args):
        return self.action()

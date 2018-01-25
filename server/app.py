from flask import Flask, Response


class App:
    app = None

    def __init__(self):
        self.app = Flask(__name__)

    def run(self):
        self.app.run()

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
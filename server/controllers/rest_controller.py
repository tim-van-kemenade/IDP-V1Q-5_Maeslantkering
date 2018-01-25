from flask import jsonify
from time import time

from server.controllers.controller_interface import ControllerInterface


class RestController(ControllerInterface):

    def add_routes(self, app):
        app.add_endpoint('/alive', 'alive', self.handle_alive_request)

    def handle_alive_request(self):
        return jsonify({
            "alive": True,
            "timestamp": time()
        })

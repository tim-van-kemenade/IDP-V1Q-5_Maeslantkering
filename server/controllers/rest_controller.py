from flask import jsonify
from time import time

from server.controllers.controller_interface import ControllerInterface


class RestController(ControllerInterface):

    def __init__(self, water_repository, storm_repository):
        self.water_repository = water_repository
        self.storm_repository = storm_repository

    def add_routes(self, app):
        app.add_endpoint('/alive', 'alive', self.handle_alive_request)
        app.add_endpoint('/water', 'water', self.handle_water_request)
        app.add_endpoint('/storm', 'storm', self.handle_storm_request)

    def handle_alive_request(self):
        return jsonify({
            "alive": True,
            "timestamp": time()
        })

    def handle_water_request(self):
        return jsonify(self.water_repository.fetch_all())

    def handle_storm_request(self):
        return jsonify(self.storm_repository.fetch_all())

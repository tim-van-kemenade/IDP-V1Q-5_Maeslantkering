from flask import Flask, jsonify, request
from time import time
import json
from server.controllers.controller_interface import ControllerInterface


class RestController(ControllerInterface):

    def __init__(self, water_repository, storm_repository):
        self.water_repository = water_repository
        self.storm_repository = storm_repository

    app = Flask(__name__)


    @app.route('/alive')
    def alive():
        # Confirms connection
        return jsonify({
            'alive': True,
            'timestamp': time()
        })

    @app.route('/water')
    def water():
        # Returns floatsensor data from dB
        return jsonify({
            'waterstand': 'test'
        })

    check = ['sorry', 'sor1', 'sor2']

    @app.route('/dbfetch')
    def dbfetch():
        # Fetches API data from the weather dB
        data = ['windsnelheidMS', 'windrichtingGR', 'windstotenMS']
        json_encode = json.dumps(data)
        return json_encode

    @app.route('/storm', methods=['POST'])
    def storm():
        # recieves JSON file and turns it into a dict
        if request.method == 'POST':
            storm_data = request.data.decode('utf-8')
            json_encode = json.loads(storm_data)

            for status in json_encode:
                global statuses
                statuses = json_encode[status]

            return jsonify({
                'datatransfer': statuses,
                'status': 'succeed'
            })

    if __name__ == '__main__':
        app.run(debug=True, host='')

    def add_routes(self, app):
        app.add_endpoint('/alive', 'alive', self.handle_alive_request)
        app.add_endpoint('/water', 'water', self.handle_water_request)
        app.add_endpoint('/storm', 'storm', self.handle_storm_request)
        app.add_endpoint('/establish', 'establish', self.handle_establish_request)

    clients = []

    def handle_establish_request(self):
        self.clients.append(request.remote_addr)
        return jsonify({
            'connection established': True,
            'timestamp': time
        })

    def handle_alive_request(self):
        return jsonify({
            "alive": True,
            "timestamp": time()
        })

    def handle_water_request(self):
        return jsonify(self.water_repository.fetch_all())

    def handle_storm_request(self):
        return jsonify(self.storm_repository.fetch_all())

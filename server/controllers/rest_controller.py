from flask import Flask, jsonify, request
from time import time
import json
from server.controllers.controller_interface import ControllerInterface


class RestController(ControllerInterface):
    clients = []

    def __init__(self, water_repository, storm_repository):
        self.water_repository = water_repository
        self.storm_repository = storm_repository

    app = Flask(__name__)

    def add_routes(self, app):
        app.add_endpoint('/establish', 'establish', self.handle_establish_request)
        app.add_endpoint('/alive', 'alive', self.handle_alive_request)
        app.add_endpoint('/water', 'water', self.handle_water_request)
        app.add_endpoint('/storm', 'storm', self.handle_storm_request)
        app.add_endpoint('/db-fetch', 'db-fetch', self.handle_dbfetch_request)

    def handle_establish_request(self):
        self.clients.append(request.remote_addr)
        return jsonify({
            'connection established': True,
            'timestamp': time()
        })

    def handle_alive_request(self):
        return jsonify({
            'alive': True,
            'timestamp': time()
        })

    def handle_water_request(self):
        return jsonify(self.water_repository.fetch_all())

    def handle_storm_request(self):
        storm_fetch = self.storm_repository.fetch_all()
        row_counter = 0
        wind_speed_list = []
        wind_burst_list = []
        epoch_list = []
        wind_graph_data = []
        for row in storm_fetch:
            row_counter += 1
            wind_speed_list.append(row[1])
            wind_burst_list.append(row[3])
            epoch_list.append(row[4])
            if row_counter == 6:
                row_counter = 0
                wind_speed = sum(wind_speed_list) / len(wind_speed_list)
                wind_burst = sum(wind_burst_list) / len(wind_burst_list)
                epoch = sum(epoch_list) / len(epoch_list)
                wind_speed_list = []
                wind_burst_list = []
                epoch_list = []
                wind_graph_data.append({'period': epoch, 'wind_speed': wind_speed, 'wind_burst': wind_burst})
        return jsonify(wind_graph_data)

    def handle_dbfetch_request(self):
        if request.method == 'POST':
            storm_data = request.data.decode('utf-8')
            json_encode = json.loads(storm_data)

            for status in json_encode:
                global statuses
                statuses = json_encode[status]

            return jsonify({
                'data_transfer': statuses,
                'status': 'succeed'
            })

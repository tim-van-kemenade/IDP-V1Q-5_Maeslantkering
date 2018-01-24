import threading
import urllib.request as request
import json

from .interface import StateInterface


class ApiState(StateInterface):
    def __init__(self, client):
        self.client = client

    def handle(self):
        success = self.get_data()
        if success == 'done':
            return 'save'
        else:
            return 'fucked'

    def request_api(self):
        """Request JSON from the buienradar.nl API URL.

        :return: dictionary containing all information from the measure stations
        """
        api_url = 'https://api.buienradar.nl/data/public/1.1/jsonfeed'
        with request.urlopen(api_url) as url:
            data = json.loads(url.read().decode())
        return data['buienradarnl']['weergegevens']['actueel_weer']['weerstations']

    def get_data(self):
        """Get necessary data from dictionary given by request_api().

        :return: done string to indicate that get_data() works
        """
        data = ApiState.request_api(self)
        data_dict = {}
        global burst_list
        burst_list = []
        for station in self.client.station_number:
            row = data['weerstation'][station[0]]
            value_list = []
            for key in self.client.key_tuple:
                value = row[key]
                if key == 'windstotenMS':
                    burst_list.append(float(value))
                value_list.append(value)
            data_dict[station[1]] = tuple(value_list)
        print(data_dict)
        t = threading.Timer(600.0, ApiState.get_data)
        t.start()
        self.client.data_dict = data_dict
        return 'done'

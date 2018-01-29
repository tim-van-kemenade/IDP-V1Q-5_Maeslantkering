import urllib.request as request
import json


class RequestApi:
    def __init__(self, client):
        self.client = client
        self.api_data = RequestApi.request_api(self)

    def request_api(self):
        api_url = 'https://api.buienradar.nl/data/public/1.1/jsonfeed'
        with request.urlopen(api_url) as url:
            data = json.loads(url.read().decode())
        print('Request sent to API')
        return data['buienradarnl']['weergegevens']['actueel_weer']['weerstations']

    def get_data(self):
        burst_list = []
        speed_list = []
        direction_list = []
        for station in self.client.station_number:
            row = self.api_data['weerstation'][station[0]]
            value_list = []
            for key in self.client.key_tuple:
                value = row[key]
                if key == 'windsnelheidMS':
                    speed_list.append(float(value))
                elif key == 'windrichtingGR':
                    direction_list.append(float(value))
                elif key == 'windstotenMS':
                    burst_list.append(float(value))
                value_list.append(value)
        average_speed = sum(speed_list)
        average_direction = sum(direction_list)
        average_burst = sum(burst_list)
        print('Got data from API')
        return [average_speed, average_direction, average_burst]

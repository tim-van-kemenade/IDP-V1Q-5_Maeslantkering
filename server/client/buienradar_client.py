import urllib.request as request
import json


class BuienRadarClient:

    station_number = (6321, 6330, 6343, 6252)

    data_keys = ('windsnelheidMS', 'windrichtingGR', 'windstotenMS')

    def get_data(self):

        api_url = 'https://api.buienradar.nl/data/public/1.1/jsonfeed'
        with request.urlopen(api_url) as url:
            data = json.loads(url.read().decode())

        filtered_data = data['buienradarnl']['weergegevens']['actueel_weer']['weerstations']['weerstation']
        print(filtered_data)
        burst_list = []
        speed_list = []
        direction_list = []
        for measure_station in filtered_data:
            if int(measure_station['@id']) in self.station_number:
                for key in self.data_keys:
                    value = measure_station[key]
                    if key == 'windsnelheidMS':
                        speed_list.append(float(value))
                    elif key == 'windrichtingGR':
                        direction_list.append(float(value))
                    elif key == 'windstotenMS':
                        burst_list.append(float(value))
        average_speed = sum(speed_list) / len(speed_list)
        average_direction = sum(direction_list) / len(direction_list)
        average_burst = sum(burst_list) / len(burst_list)
        value_list = [average_speed, average_direction, average_burst]
        print(value_list)
        return value_list

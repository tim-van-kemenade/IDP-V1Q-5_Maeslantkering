import urllib.request as request
import json


class BuienRadarClient:

    station_number = (
        (8, 'Euro_platform'),
        (16, 'Hoek_van_Holland'),
        (33, 'Rotterdam_Geulhaven'),
        (51, 'Zeeplatform_K13')
    )

    data_keys = ('windsnelheidMS', 'windrichtingGR', 'windstotenMS')

    def get_data(self):

        api_url = 'https://api.buienradar.nl/data/public/1.1/jsonfeed'
        with request.urlopen(api_url) as url:
            data = json.loads(url.read().decode())

        filtered_data = data['buienradarnl']['weergegevens']['actueel_weer']['weerstations']

        burst_list = []
        speed_list = []
        direction_list = []
        for station in self.station_number:
            row = filtered_data['weerstation'][station[0]]
            value_list = []
            for key in self.data_keys:
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

        return [average_speed, average_direction, average_burst]

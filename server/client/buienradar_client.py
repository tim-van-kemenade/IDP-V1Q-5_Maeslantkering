import urllib.request as request
import json


class BuienRadarClient:
    """Class where buienradar.nl weather data is requested and parsed."""
    station_number = (6321, 6330, 6343, 6252)

    data_keys = ('windsnelheidMS', 'windrichtingGR', 'windstotenMS')

    def get_data(self):
        """Get data from buienradar.nl and get specified data in data_keys from the stations specified in
        station_number.
        """
        api_url = 'https://api.buienradar.nl/data/public/1.1/jsonfeed'
        with request.urlopen(api_url) as url:
            data = json.loads(url.read().decode())
        # Jump into the array/list containing the requested data
        filtered_data = data['buienradarnl']['weergegevens']['actueel_weer']['weerstations']['weerstation']
        print(filtered_data)
        burst_list = []
        speed_list = []
        direction_list = []
        for measure_station in filtered_data:  # Check every row (each row is a measure station)
            if int(measure_station['@id']) in self.station_number:  # If id matches a station number continue in row
                for key in self.data_keys:
                    value = measure_station[key]
                    if key == 'windsnelheidMS':  # If key is windsnelheidMS append data
                        speed_list.append(float(value))
                    elif key == 'windrichtingGR':  # If key is windrichtingGR append data
                        direction_list.append(float(value))
                    elif key == 'windstotenMS':  # If key is windstotenMS append data
                        burst_list.append(float(value))
        # Below averages are calculated
        average_speed = sum(speed_list) / len(speed_list)
        average_direction = sum(direction_list) / len(direction_list)
        average_burst = sum(burst_list) / len(burst_list)
        value_list = [average_speed, average_direction, average_burst]  # Insert averages into list and return the list
        print(value_list)
        return value_list

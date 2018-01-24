import threading
import urllib.request as request
import json

station_number = ((8, 'Euro_platform'),
                  (16, 'Hoek_van_Holland'),
                  (33, 'Rotterdam_Geulhaven'),
                  (51, 'Zeeplatform_K13')
                  )
key_tuple = ('windsnelheidMS', 'windrichtingGR', 'windstotenMS')\


def request_api():
    """Request JSON from the buienradar.nl API URL.

    :return: dictionary containing all information from the measure stations
    """
    api_url = 'https://api.buienradar.nl/data/public/1.1/jsonfeed'
    with request.urlopen(api_url) as url:
        data = json.loads(url.read().decode())
    return data['buienradarnl']['weergegevens']['actueel_weer']['weerstations']


def get_data():
    """Get necessary data from dictionary given by request_api().

    :return: done string to indicate that get_data() works
    """
    data = request_api()
    burst_list = []
    speed_list = []
    direction_list = []
    for station in station_number:
        row = data['weerstation'][station[0]]
        value_list = []
        for key in key_tuple:
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
    global data_list
    data_list = [average_speed, average_direction, average_burst]
    t = threading.Timer(600.0, get_data)
    t.start()
    return 'done'


def storm_code(wind_burst):
    """Determines if the average wind burst is code orange or code yellow.

    :param wind_burst: float of recorded wind_burst average from measure stations selected in get_data()
    :return: storm status, returns 'yellow' for code yellow and 'orange' for code orange, else 'None'
    """
    if wind_burst > 27.777778:
        storm = 'orange'
    elif wind_burst > 20.833333:
        storm = 'yellow'
    else:
        storm = None
    return storm


if __name__ == '__main__':
    print(23)
    get_data()
    while True:
        storm_code(data_list[2])

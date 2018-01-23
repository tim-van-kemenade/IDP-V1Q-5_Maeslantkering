import threading
import urllib.request as request
import json
import sqlite3
import time

station_number = ((8, 'Euro_platform'),
                  (16, 'Hoek_van_Holland'),
                  (33, 'Rotterdam_Geulhaven'),
                  (50, 'Zeeplatform_F-3'),
                  (51, 'Zeeplatform_K13')
                  )
key_tuple = ('windsnelheidMS', 'windrichtingGR', 'windrichting', 'windstotenMS')
create_storm = 'CREATE TABLE IF NOT EXISTS storm (' \
               'id INTEGER PRIMARY KEY AUTOINCREMENT,' \
               'meet_station_id INTEGER,' \
               'windsnelheidMS REAL,' \
               'windrichtingGR INTEGER,' \
               'windstotenMS REAL,' \
               'epoch REAL' \
               ');'.format(key_tuple[0], key_tuple[1], key_tuple[3])
create_water = 'CREATE TABLE IF NOT EXISTS water_data (' \
                   'id INTEGER PRIMARY KEY AUTOINCREMENT,' \
                   'average_height REAL,' \
                   'epoch REAL' \
                   ');'
insert_storm = 'INSERT INTO storm (windsnelheidMS, windrichtingGR, windstotenMS, epoch)' \
               'VALUES({}, {}, {}, {});'
insert_water = 'INSERT INTO water_data (average_height, epoch)' \
               'VALUES ({}, {});'


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
    data_dict = {}
    global burst_list
    burst_list = []
    for station in station_number:
        row = data['weerstation'][station[0]]
        value_list = []
        for key in key_tuple:
            value = row[key]
            if key == 'windstotenMS':
                burst_list.append(float(value))
            value_list.append(value)
        data_dict[station[1]] = tuple(value_list)
    print(data_dict)
    t = threading.Timer(600.0, get_data)
    t.start()
    loop_query(data_dict)
    return 'done'


def loop_query(data_dict):
    """Format query's from data given by the API and write it to the database.

    :param data_dict: dictionary from the API passed on by get_data()
    :return: done string to indicate that loop_query() works
    """
    epoch = time.time()
    for measure_station in station_number:
        data_tuple = data_dict[measure_station[1]]
        query = format_query('storm', data_tuple, epoch)
        database_control('Weather.db', query)
    return 'done'


def format_query(table_name, data_tuple, epoch):
    """Creates a query with the proper data included.

    :param table_name: determines the name of the table
    :param data_tuple: tuple used to pass on data accessed by index
    :param epoch: time in seconds since epoch
    :return: query to be used on the database
    """
    if table_name == 'storm':
        query = insert_storm.format(data_tuple[0], data_tuple[1], data_tuple[3], epoch)
    elif table_name == 'water_data':
        query = insert_water.format(data_tuple[0], epoch)
    else:
        print('Error. You fucked up!')
        query = ''
    return query


def database_control(database, query, fetch=False):
    """Establish connection with database and start transaction.

    :param database: name of the database with which a connection is established
    :param query: SQL-statement send to the database
    :param fetch: if True data will be fetched(default False)
    :return: fetched data if fetch is True otherwise return if transaction was successful
    """
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    if fetch is True:
        data = cursor.fetchall()
    else:
        data = None
    connection.close()
    return data


def storm_code(wind_bursts):
    """Determines if the average wind burst is code orange or code yellow.

    :param wind_bursts: tuple of recorded wind_bursts from measure stations selected in get_data()
    :return: storm status, returns 'yellow' for code yellow and 'orange' for code orange, else 'None'
    """
    average_burst = sum(wind_bursts) / len(wind_bursts)
    if average_burst > 27.777778:
        storm = 'orange'
    elif average_burst > 20.833333:
        storm = 'yellow'
    else:
        storm = None
    return storm


if __name__ == '__main__':
    database_control('Weather.db', create_water)
    database_control('Weather.db', create_storm)
    get_data()
    while True:
        alert_code = storm_code(tuple(burst_list))
        time.sleep(2)

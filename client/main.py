import threading
import urllib.request as request
import json
import sqlite3

station_number = ((8, 'Euro_platform'),
                  (16, 'Hoek_van_Holland'),
                  (33, 'Rotterdam_Geulhaven'),
                  (50, 'Zeeplatform_F-3'),
                  (51, 'Zeeplatform_K13')
                  )
key_tuple = ('windsnelheidMS', 'windrichtingGR', 'windrichting', 'windstotenMS')


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

    :return: dictionary ordered by measure stations names as keys with requested data as value in a tuple
    """
    data = request_api()
    data_dict = {}
    for station in station_number:
        row = data['weerstation'][station[0]]
        value_list = []
        for key in key_tuple:
            value = row[key]
            value_list.append(value)
        data_dict[station[1]] = tuple(value_list)
    print(data_dict)
    t = threading.Timer(5.0, get_data)
    t.start()
    return data_dict


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
        return data, 'okay'
    connection.close()
    return 'okay'


if __name__ == '__main__':
    get_data()

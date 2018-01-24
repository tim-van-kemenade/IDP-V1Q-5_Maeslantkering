import sqlite3
import time

from .interface import StateInterface


class SaveState(StateInterface):
    create_storm = 'CREATE TABLE IF NOT EXISTS storm (' \
                   'id INTEGER PRIMARY KEY AUTOINCREMENT,' \
                   'meet_station_id INTEGER,' \
                   'windsnelheidMS REAL,' \
                   'windrichtingGR INTEGER,' \
                   'windstotenMS REAL,' \
                   'epoch REAL' \
                   ');'
    create_water = 'CREATE TABLE IF NOT EXISTS water_data (' \
                   'id INTEGER PRIMARY KEY AUTOINCREMENT,' \
                   'average_height REAL,' \
                   'epoch REAL' \
                   ');'
    insert_storm = 'INSERT INTO storm (windsnelheidMS, windrichtingGR, windstotenMS, epoch)' \
                   'VALUES({}, {}, {}, {});'
    insert_water = 'INSERT INTO water_data (average_height, epoch)' \
                   'VALUES ({}, {});'

    def __init__(self, client, database):
        self.client = client
        self.database = database
        SaveState.database_control(self, SaveState.create_storm)
        SaveState.database_control(self, SaveState.create_water)

    def handle(self):
        saved = SaveState.loop_query(self, self.client.data_dict)
        print(saved)
        if saved == 'success':
            return 'api'
        else:
            return 'fucked'

    def loop_query(self, data_dict):
        """Format query's from data given by the API and write it to the database.

        :param data_dict: dictionary from the API passed on by get_data()
        :return: done string to indicate that loop_query() works
        """
        epoch = time.time()
        for measure_station in self.client.station_number:
            data_tuple = data_dict[measure_station[1]]
            query = SaveState.format_query(self, 'storm', data_tuple, epoch)
            SaveState.database_control(self, query)
        return 'success'

    def format_query(self, table_name, data_tuple, epoch):
        """Creates a query with the proper data included.

        :param table_name: determines the name of the table
        :param data_tuple: tuple used to pass on data accessed by index
        :param epoch: time in seconds since epoch
        :return: query to be used on the database
        """
        if table_name == 'storm':
            query = SaveState.insert_storm.format(data_tuple[0], data_tuple[1], data_tuple[3], epoch)
        elif table_name == 'water_data':
            query = SaveState.insert_water.format(data_tuple[0], epoch)
        else:
            print('Error. You fucked up!')
            query = ''
        return query

    def database_control(self, query, fetch=False):
        """Establish connection with database and start transaction.

        :param database: name of the database with which a connection is established
        :param query: SQL-statement send to the database
        :param fetch: if True data will be fetched(default False)
        :return: fetched data if fetch is True otherwise return if transaction was successful
        """
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        if fetch is True:
            data = cursor.fetchall()
        else:
            data = None
        connection.close()
        return data

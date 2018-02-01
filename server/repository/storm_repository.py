import time


class StormRepository:
    """Class containing functions to execute queries on water database."""
    def __init__(self, connection):
        self.connection = connection
        self.create_table()

    def create_table(self):
        self.connection.execute(
            'CREATE TABLE IF NOT EXISTS storm ('
            'id INTEGER PRIMARY KEY AUTOINCREMENT,'
            'windsnelheidMS REAL,'
            'windrichtingGR INTEGER,'
            'windstotenMS REAL,'
            'epoch REAL'
            ');'
        )
        self.connection.commit()
        print('Storm table exists')

    def add_data(self, wind_speed, wind_direction, wind_burst):
        print(wind_speed, wind_direction, wind_burst, '- Add data storm repository')
        self.connection.execute('INSERT INTO storm (windsnelheidMS, windrichtingGR, windstotenMS, epoch)'
                                'VALUES({}, {}, {}, {});'.format(wind_speed,
                                                                 wind_direction,
                                                                 wind_burst,
                                                                 time.time()
                                                                 )
                                )
        self.connection.commit()

    def fetch_all(self):
        cursor = self.connection.cursor()
        cursor.execute('SELECT * FROM storm ORDER BY id DESC')
        print('Fetched all storm data - Storm table')
        return cursor.fetchall()

    def fetch_graph_data(self):
        cursor = self.connection.cursor()
        cursor.execute('SELECT   id, windsnelheidMS, windstotenMS, epoch FROM storm ORDER BY id DESC LIMIT 42')
        print('Fetched last 42 wind burst rows - Storm table')
        return cursor.fetchall()

    def fetch_latest_wind_speed(self):
        cursor = self.connection.cursor()
        cursor.execute('SELECT id, windsnelheidMS, epoch FROM storm ORDER BY id DESC LIMIT 0,1')

        return cursor.fetchall()

    def fetch_current_direction(self):
        cursor = self.connection.cursor()
        cursor.execute('SELECT windrichtingGR, epoch FROM storm ORDER BY id DESC')
        print('Fetched last direction row - Storm table')
        return cursor.fetchone()

    def fetch_last_row(self):
        cursor = self.connection.cursor()
        cursor.execute('SELECT * FROM storm ORDER BY id DESC LIMIT 1')
        print('Fetched last row - Storm table')
        return cursor.fetchall()

import time


class StormRepository:
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

    def add_data(self, wind_speed, wind_direction, wind_burst):
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
        return cursor.fetchall()

    def fetch_wind_burst(self):
        cursor = self.connection.cursor()
        cursor.execute('SELECT   id, windstotenMS FROM storm ORDER BY id DESC LIMIT 42')
        return cursor.fetchall()

    def fetch_wind_speed(self):
        cursor = self.connection.cursor()
        cursor.execute('SELECT id, windsnelheidMS FROM storm ORDER BY id DESC LIMIT 42')
        return cursor.fetchall()

    def fetch_current_direction(self):
        cursor = self.connection.cursor()
        cursor.execute('SELECT windrichtingGR FROM storm ORDER BY id DESC')
        return cursor.fetchone()

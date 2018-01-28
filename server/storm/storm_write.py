from server.factory.database_factory import DatabaseFactory
from server.repository.storm_repository import StormRepository


class StormWrite:
    def __init__(self, data_list):
        self.data = data_list

    def storm_code(self):
        if self.data[2] > 27.777778:
            storm = 'orange'
        elif self.data[2] > 20.833333:
            storm = 'yellow'
        else:
            storm = None
        return storm

    def storm_table_write(self):
        database = DatabaseFactory()  # TODO: properly create an instance for DatabaseFactory
        connection = database.create_connection()  # TODO: if above is completed check if sqlite functions get executed
        repository = StormRepository(connection)
        repository.add_data(self.data[0], self.data[1], self.data[2])

from server.worker.abstract_worker import AbstractWorker


class APIWorker(AbstractWorker):

    def get_timeout(self) -> int:
        return 60

    def __init__(self, buienradar_client):
        self.client = buienradar_client

    def handle(self):
        print('Getting API data')
        api_data = self.client.get_data()
        #MainClass.data_list = api_data.get_data()
        print('Saving API data in database')
        #storm_write = StormWrite(self.connection, MainClass.data_list)
        #storm_write.storm_table_write()
        #MainClass.storm = storm_write.storm_code()
        print('Saved API data in database')
        #storm_repository = StormRepository(self.connection)
        print('Check if data is saved')
        #fetch_epoch_storm = storm_repository.fetch_last_row()
        #print(fetch_epoch_storm, '- Storm table')
        #time.sleep(600)
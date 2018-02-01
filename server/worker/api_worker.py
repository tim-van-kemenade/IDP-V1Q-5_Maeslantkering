from server.worker.abstract_worker import AbstractWorker


class APIWorker(AbstractWorker):

    def get_timeout(self) -> int:
        return 600

    def __init__(self, buienradar_client, storm_repository):
        self.client = buienradar_client
        self.repository = storm_repository

    def handle(self):
        print('Getting API data')
        api_data = self.client.get_data()
        print('Saving API data in database')
        self.repository.add_data(api_data[0], api_data[1], api_data[2])
        print('Saved API data in database')
        last_row = self.repository.fetch_last_row()
        print('Check if data is saved')
        print(last_row, '- Storm table')

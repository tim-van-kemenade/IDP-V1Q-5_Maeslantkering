import threading
import time

from server.app import App
from server.controllers.rest_controller import RestController
from server.IO.hardware import Hardware
from server.states.open_state import OpenState
from server.states.closed_state import ClosedState
from server.states.opening_state import OpeningState
from server.states.closing_state import ClosingState
from server.storm.request_api import RequestApi
from server.storm.storm_write import StormWrite
from server.factory.database_factory import DatabaseFactory
from server.repository.water_repository import WaterRepository
from server.repository.storm_repository import StormRepository


class MainClass:
    storm = None
    data_list = [0, 0, 0]  # Used in child class
    station_number = ((8, 'Euro_platform'),
                      (16, 'Hoek_van_Holland'),
                      (33, 'Rotterdam_Geulhaven'),
                      (51, 'Zeeplatform_K13')
                      )  # Used in child class
    key_tuple = ('windsnelheidMS', 'windrichtingGR', 'windstotenMS')  # Used in child class

    state = 'open'
    states = {}

    def __init__(self):
        self.connection = DatabaseFactory().create_connection()
        self.water_repository = WaterRepository(self.connection)
        self.storm_repository = StormRepository(self.connection)

        self.hardware = Hardware()
        self.flask_app = App()

        self.register_controllers()

        self.states = {
            'open': OpenState(self, self.hardware, MainClass.storm).handle(),
            'closed': ClosedState(self, self.hardware, MainClass.storm).handle(),
            'opening': OpeningState(self, self.hardware).handle(),
            'closing': ClosingState(self, self.hardware).handle()
        }

        flask_thread = threading.Thread(target=self.flask_app.run)
        flask_thread.start()

        state_thread = threading.Thread(target=self.state_change)
        state_thread.start()

        api_thread = threading.Thread(self.data_save())
        api_thread.start()

    def register_controllers(self):
        self.flask_app.register_controller(RestController(self.water_repository, self.storm_repository))

    def state_change(self):
        while True:
            self.state = self.states[self.state]

    def data_save(self):
        while True:
            api_data = RequestApi(self)
            MainClass.data_list = api_data.get_data()
            storm_write = StormWrite(MainClass.data_list)
            storm_write.storm_table_write()
            MainClass.storm = storm_write.storm_code()
            time.sleep(600)


if __name__ == '__main__':
    server = MainClass()

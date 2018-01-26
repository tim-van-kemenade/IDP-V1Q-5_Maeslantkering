import threading

import sqlite3
from server.app import App
from server.controllers.rest_controller import RestController
from server.IO.hardware import Hardware
from server.states.open_state import OpenState
from server.states.closed_state import ClosedState
from server.states.opening_state import OpeningState
from server.states.closing_state import ClosingState

from server.factory.database_factory import DatabaseFactory
from server.repository.water_repository import WaterRepository
from server.repository.storm_repository import StormRepository


class MainClass:
    storm = None

    state: str = 'open'
    states: dict = {}

    hardware: Hardware
    flask_app: App

    connection: sqlite3.Connection
    water_repository: WaterRepository
    storm_repository: StormRepository

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

        state_thread = threading.Thread(self.state_change())
        state_thread.start()

    def register_controllers(self):
        self.flask_app.register_controller(RestController(self.water_repository, self.storm_repository))

    def state_change(self):
        while True:
            self.state = self.states[self.state]


if __name__ == '__main__':
    server = MainClass()
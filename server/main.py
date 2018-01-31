import threading

from server.app import App
from server.controllers.rest_controller import RestController
from server.controllers.gate_controller import GateController
from server.IO.hardware import Hardware
from server.states.open_state import OpenState
from server.states.closed_state import ClosedState
from server.states.force_closed_state import ForceClosedState
from server.states.force_open_state import ForceOpenState
from server.factory.database_factory import DatabaseFactory
from server.repository.water_repository import WaterRepository
from server.repository.storm_repository import StormRepository
from server.client.buienradar_client import BuienRadarClient
from server.state_machine import StateMachine
from server.worker.api_worker import APIWorker
from server.worker.storm_worker import StormWorker


class MainClass:
    storm = None
    data_list = [0, 0, 0]  # Used in child class

    state = 'open'
    current_state = None

    def __init__(self):
        self.connection = DatabaseFactory().create_connection()
        self.water_repository = WaterRepository(self.connection)
        self.storm_repository = StormRepository(self.connection)
        self.buienradar_client = BuienRadarClient()

        self.hardware = Hardware()
        self.flask_app = App()

        self.state_machine = StateMachine({
            'open': OpenState(self.hardware),
            'closed': ClosedState(self.hardware),
            'force-open': ForceOpenState(self.hardware),
            'force-closed': ForceClosedState(self.hardware)
        })

        self.workers = [
            APIWorker(self.buienradar_client, self.storm_repository),
            StormWorker(self.state_machine, self.hardware)
        ]

        self.register_controllers()
        self.register_workers()

        self.flask_app.run()

    def register_controllers(self):
        self.flask_app.register_controller(
            RestController(self.water_repository, self.storm_repository)
        )

        self.flask_app.register_controller(
            GateController(self.state_machine)
        )

    def register_workers(self):
        for worker in self.workers:
            worker_thread = threading.Thread(target=worker.run)
            worker_thread.start()


if __name__ == '__main__':
    server = MainClass()

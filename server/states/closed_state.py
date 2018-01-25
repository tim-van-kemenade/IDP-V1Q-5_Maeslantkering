import time

from .state_interface import StateInterface


class ClosedState(StateInterface):
    sensor_1 = 13
    sensor_2 = 15

    def __init__(self, client, hardware, storm):
        self.client = client
        self.hardware = hardware
        self.storm = storm

    def handle(self):
        if self.storm is True:
            input_1 = self.hardware.handle_input(ClosedState.sensor_2)
            time.sleep(2)
            input_2 = self.hardware.handle_input(ClosedState.sensor_2)
        else:
            input_1 = self.hardware.handle_input(ClosedState.sensor_1)
            time.sleep(2)
            input_2 = self.hardware.handle_input(ClosedState.sensor_1)
        if input_1 is False and input_2 is False:
            return 'opening'
        else:
            return 'closed'

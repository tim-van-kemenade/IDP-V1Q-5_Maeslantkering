import time

from .state_interface import StateInterface


class OpenState(StateInterface):
    sensor_1 = 13
    sensor_2 = 15

    def __init__(self, client, hardware, storm):
        self.client = client
        self.hardware = hardware
        self.storm = storm

    def handle(self):
        if self.storm is True:
            input_1 = self.hardware.handle_input(OpenState.sensor_2)
            time.sleep(3)
            input_2 = self.hardware.handle_input(OpenState.sensor_2)
        else:
            input_1 = self.hardware.handle_input(OpenState.sensor_1)
            time.sleep(3)
            input_2 = self.hardware.handle_input(OpenState.sensor_1)
        if input_1 is True and input_2 is True:
            return 'closing'
        else:
            return 'open'

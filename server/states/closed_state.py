import time

from .state_interface import StateInterface


class ClosedState(StateInterface):
    sensor_1 = 13
    sensor_2 = 15

    def __init__(self, client, hardware, storm):
        self.client = client
        self.hardware = hardware
        self.storm = storm
        print('__init__ closed state finished')

    def handle(self):
        if self.storm is True:
            input_1 = self.hardware.float_sensor(ClosedState.sensor_2)
            time.sleep(2)
            input_2 = self.hardware.float_sensor(ClosedState.sensor_2)
        else:
            input_1 = self.hardware.float_sensor(ClosedState.sensor_1)
            time.sleep(2)
            input_2 = self.hardware.float_sensor(ClosedState.sensor_1)
        print('Checked float sensor inputs - Closed state\nInput 1: {}\nInput 2: {}'.format(input_1, input_2))
        if input_1 is False and input_2 is False:
            return 'opening'
        else:
            return 'closed'

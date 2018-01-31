from .state_interface import StateInterface


class ForceClosedState(StateInterface):
    def __init__(self, hardware):
        self.hardware = hardware

    def handle(self):
        self.hardware.close_gate()

    def green(self):
        self.hardware.green_off()

    def red(self):
        self.hardware.red_on()

import time

from .state_interface import StateInterface


class OpenState(StateInterface):

    def __init__(self, hardware):
        self.hardware = hardware

    def handle(self):
        self.hardware.open_gate()


import time
from .state_interface import StateInterface

class OpenState(StateInterface):
    """Open state, gate opens and red light turns off."""
    def __init__(self, hardware):
        self.hardware = hardware

    def handle(self):
        self.hardware.open_gate()
        self.hardware.red_off()
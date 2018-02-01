from .state_interface import StateInterface


class ClosedState(StateInterface):
    """Closed state, gate closes and red light turns on."""
    def __init__(self, hardware):
        self.hardware = hardware

    def handle(self):
        self.hardware.close_gate()
        self.hardware.red_on()

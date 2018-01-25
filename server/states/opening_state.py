from .state_interface import StateInterface


class OpeningState(StateInterface):
    def __init__(self, client, hardware):
        self.client = client
        self.hardware = hardware

    def handle(self):
        self.hardware.open_gate()
        return 'open'

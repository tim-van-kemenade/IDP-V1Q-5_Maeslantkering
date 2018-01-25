from .state_interface import StateInterface


class ClosingState(StateInterface):
    def __init__(self, client, hardware):
        self.client = client
        self.hardware = hardware

    def handle(self):
        self.hardware.close_gate()
        return 'closed'

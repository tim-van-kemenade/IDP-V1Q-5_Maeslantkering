from .state_interface import StateInterface


class OpeningState(StateInterface):
    def __init__(self, client, hardware):
        self.client = client
        self.hardware = hardware
        print('__init__ opening state finished')

    def handle(self):
        self.hardware.open_gate()
        print('Gate opened')
        return 'open'

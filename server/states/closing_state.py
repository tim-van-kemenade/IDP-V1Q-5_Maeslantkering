from .state_interface import StateInterface


class ClosingState(StateInterface):
    def __init__(self, client, hardware):
        self.client = client
        self.hardware = hardware
        print('__init__ closing state finished')

    def handle(self):
        self.hardware.close_gate()
        print('Closed gate')
        return 'closed'

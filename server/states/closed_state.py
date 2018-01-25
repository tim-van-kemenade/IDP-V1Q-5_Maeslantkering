
from .state_interface import StateInterface


class ClosedState(StateInterface):
    def handle(self):
        print('Closed!')
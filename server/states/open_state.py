
from .state_interface import StateInterface


class OpenState(StateInterface):
    def handle(self):
        print('Open!')
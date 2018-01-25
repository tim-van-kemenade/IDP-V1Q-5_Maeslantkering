
from .state_interface import StateInterface


class OpeningState(StateInterface):
    def handle(self):
        print('Opening!')
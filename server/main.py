import threading

from server.app import App
from server.controllers.rest_controller import RestController
from server.IO.hardware import Hardware
from server.states.open_state import OpenState
from server.states.closed_state import ClosedState
from server.states.opening_state import OpeningState
from server.states.closing_state import ClosingState


class MainClass:
    storm = None
    state = 'open'

    def __init__(self):
        self.hardware = Hardware()
        self.states = {
            'open': OpenState(self, self.hardware, MainClass.storm).handle(),
            'closed': ClosedState(self, self.hardware, MainClass.storm).handle(),
            'opening': OpeningState(self, self.hardware).handle(),
            'closing': ClosingState(self, self.hardware).handle()
        }
        state_thread = threading.Thread(self.state_change())
        state_thread.start()

    def state_change(self):
        while True:
            self.state = self.states[self.state]


app = App()

app.register_controller(RestController)

if __name__ == '__main__':
    server = MainClass()
    app.run()

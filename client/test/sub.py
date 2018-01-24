from client.test.state.save_state import SaveState
from client.test.state.api_state import ApiState


class MainClient(object):
    station_number = ((8, 'Euro_platform'),
                      (16, 'Hoek_van_Holland'),
                      (33, 'Rotterdam_Geulhaven'),
                      (50, 'Zeeplatform_F-3'),
                      (51, 'Zeeplatform_K13')
                      )
    key_tuple = ('windsnelheidMS', 'windrichtingGR', 'windrichting', 'windstotenMS')
    database = 'Weather.db'
    alarm_state = 'api'
    data_dict = {}

    def __init__(self):
        # self.hardware = Hardware()
        self.states = {
            'save': SaveState(self, MainClient.database),
            'api': ApiState(self)
        }
        self.run_alarm()

    def run_alarm(self):
        while True:
            state_class = self.states[self.alarm_state]
            self.alarm_state = state_class.handle()


if __name__ == '__main__':
    client = MainClient()

from server.worker.abstract_worker import AbstractWorker


class StormWorker(AbstractWorker):

    def __init__(self, state_machine, hardware):
        self.state_machine = state_machine
        self.hardware = hardware

    def handle(self):
        print('Storm worker, lets make some decisions!  ')

        current_state = self.state_machine.get_current_state()
        if current_state == 'force-open' or current_state == 'force-closed':
            print('forced!')
            return

        score = self.get_sensor_score()

        if score > 0:
            self.state_machine.apply_state('open')
        else:
            self.state_machine.apply_state('closed')

    def get_timeout(self) -> int:
        return 1

    def get_storm_code_by_score(self, score) -> str:
        if score > 27.777778:
            return 'orange'
        elif score > 20.833333:
            return 'yellow'

        return 'none'

    def get_sensor_score(self):
        lower_input = self.hardware.get_lower_float_sensor().value
        higher_input = self.hardware.get_higher_float_sensor().value

        if lower_input and higher_input:
            return 2

        if lower_input:
            return 1

        return 0

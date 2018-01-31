from server.worker.abstract_worker import AbstractWorker


class StormWorker(AbstractWorker):

    last_saved_sensor_score = 0

    def __init__(self, state_machine, hardware, water_repository, storm_repository):
        self.state_machine = state_machine
        self.hardware = hardware
        self.water_repository = water_repository
        self.storm_repository = storm_repository

    def handle(self):

        current_state = self.state_machine.get_current_state()
        if current_state == 'force-open' or current_state == 'force-closed':
            return

        score = self.get_sensor_score()
        code = self.get_storm_code()

        if score == 1 and code != 'none':
            self.state_machine.apply_state('closed')
        elif score == 2:
            self.state_machine.apply_state('closed')
        else:
            self.state_machine.apply_state('open')

        if self.last_saved_sensor_score != score:
            self.water_repository.add_data(score)
            self.last_saved_sensor_score = score

    def get_timeout(self) -> int:
        return 1

    def get_storm_code(self) -> str:
        data = self.storm_repository.fetch_latest_wind_speed()
        score = data[0]['windsnelheidMS']

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

from server.worker.abstract_worker import AbstractWorker


class StormWorker(AbstractWorker):
    """Storm worker handles basic gate action, like open and close with the needed data retrieval."""
    last_saved_sensor_score = 0

    def __init__(self, state_machine, hardware, water_repository, storm_repository):
        self.state_machine = state_machine
        self.hardware = hardware
        self.water_repository = water_repository
        self.storm_repository = storm_repository

    def handle(self):

        current_state = self.state_machine.get_current_state()
        if current_state == 'force-open' or current_state == 'force-closed':  # do nothing if gate is in forced state
            return

        score = self.get_sensor_score()
        code = self.get_storm_code()

        if score == 1 and code != 'none':  # if the lowest sensor returned 1 and storm code is not none close gate
            self.state_machine.apply_state('closed')
        elif score == 2:  # if both sensors returned 1 (the sum of both is 2) close gate
            self.state_machine.apply_state('closed')
        else:  # if above none of the above is true open
            self.state_machine.apply_state('open')

        if self.last_saved_sensor_score != score:  # save sensor data if score changed
            self.water_repository.add_data(score)
            self.last_saved_sensor_score = score

    def get_timeout(self) -> int:
        return 1

    def get_storm_code(self) -> str:
        """Checks if a storm code, which signals a faster gate close, is active based on set values from KMNI."""
        data = self.storm_repository.fetch_latest_wind_speed()

        if not data:
            return 'none'

        score = data[0]['windsnelheidMS']  # data previously fetched filtered on key to check the wind speed

        if score > 27.777778:  # code orange for wind speed starts at 27.78 m/s (100 km/h) according to the KMNI
            return 'orange'
        elif score > 20.833333:  # code yellow for wind speed starts at 20.83 m/s (75 km/h) according to KMNI
            return 'yellow'

        return 'none'  # returns none if no storm is present

    def get_sensor_score(self):
        """Get sensor input to determine a score (0, 1 or 2) to determine if gate should close automatically."""
        lower_input = self.hardware.get_lower_float_sensor().value
        higher_input = self.hardware.get_higher_float_sensor().value

        print('low ', lower_input)
        print('high', higher_input)

        if lower_input and higher_input:
            return 2

        if lower_input:
            return 1

        return 0

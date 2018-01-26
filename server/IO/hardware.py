from gpiozero import Motor


class Hardware(object):
    servo = 11
    sensor_1 = 13

    def __init__(self):
        self.motor = Motor(forward=11, backward=50, pwm=False)

    def handle_input(self, input):
        # todo: find out how to do this @ gpiozero
        return 0

    def open_gate(self) -> bool:
        self.motor.forward()
        return False

    def close_gate(self) -> bool:
        self.motor.backward()
        return True

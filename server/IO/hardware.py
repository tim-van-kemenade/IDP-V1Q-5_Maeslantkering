from gpiozero import Servo


class Hardware(object):
    servo_pin = 11
    sensor_1 = 13

    def __init__(self):
        self.servo = Servo(self.servo_pin)

    def handle_input(self, input):
        # todo: find out how to do this @ gpiozero
        return 0

    def open_gate(self) -> bool:
        self.servo.min()
        return False

    def close_gate(self) -> bool:
        self.servo.max()
        return True

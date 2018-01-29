from gpiozero import Servo, MotionSensor
from gpiozero.pins import mock
import platform


class Hardware(object):
    servo_pin = 17

    def __init__(self):
        if platform.system() == 'Linux':
            self.servo = Servo(self.servo_pin)
        else:
            self.servo = Servo(self.servo_pin, pin_factory=mock.MockFactory(pin_class=mock.MockPWMPin))

    def float_sensor(self, pin):
        # todo: find out how to do this @ gpiozero
        sensor = MotionSensor(pin)
        feedback = sensor.wait_for_inactive()
        return feedback

    def open_gate(self) -> bool:
        self.servo.min()
        return False

    def close_gate(self) -> bool:
        self.servo.max()
        return True

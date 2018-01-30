from gpiozero import Servo, MotionSensor, InputDevice, OutputDevice
from gpiozero.pins import mock
import platform


class Hardware(object):

    servo_pin = 17
    lower_float_pin = 27
    higher_float_pin = 15

    def __init__(self):
        if platform.system() == 'Linux':
            self.servo = Servo(self.servo_pin)
        else:
            self.servo = Servo(
                self.servo_pin,
                pin_factory=mock.MockFactory(pin_class=mock.MockPWMPin)
            )

    def get_lower_float_sensor(self):
        return OutputDevice(self.lower_float_pin)

    def get_higher_float_sensor(self):
        return OutputDevice(self.higher_float_pin)

    def open_gate(self):
        self.servo.min()

    def close_gate(self):
        self.servo.max()

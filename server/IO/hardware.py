from gpiozero import Servo, OutputDevice
from gpiozero.pins import mock
import platform
from gpiozero import LED


class Hardware(object):
    """Set-up hardware with gpiozero."""
    servo_pin = 17
    lower_float_pin = 18
    higher_float_pin = 22

    def __init__(self):
        self.red = LED(3)
        self.lower_sensor = OutputDevice(self.lower_float_pin)
        self.higher_sensor = OutputDevice(self.higher_float_pin)

        if platform.system() == 'Linux':
            self.servo = Servo(self.servo_pin)
        else:
            self.servo = Servo(
                self.servo_pin,
                pin_factory=mock.MockFactory(pin_class=mock.MockPWMPin)
            )

    def get_lower_float_sensor(self):
        return self.lower_sensor

    def get_higher_float_sensor(self):
        return self.higher_sensor

    def open_gate(self):
        self.servo.max()

    def close_gate(self):
        self.servo.min()

    def red_on(self):
        return self.red.on()

    def red_off(self):
        return self.red.off()

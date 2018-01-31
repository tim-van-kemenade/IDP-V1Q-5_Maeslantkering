from gpiozero import Servo, MotionSensor, InputDevice, OutputDevice
from gpiozero.pins import mock
import platform
from gpiozero import LED


class Hardware(object):

    servo_pin = 17
    lower_float_pin = 27
    higher_float_pin = 15
    green = LED(2)
    red = LED(3)

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

    def green_on(self, green):
        return green.on()

    def red_on(self, red):
        return red.on()

    def green_off(self, green):
        return green.off()

    def red_off(self, red):
        return red.off()

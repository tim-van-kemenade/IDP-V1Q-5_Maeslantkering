import RPi.GPIO as GPIO
import time


class Hardware(object):
    servo = 11
    sensor_1 = 13
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(servo, GPIO.OUT)
    GPIO.setup(sensor_1, GPIO.OUT)
    servo_pwm = GPIO.PWM(servo, 50)
    servo_pwm.start(1.9)

    def __init__(self):
        print('nothing special')

    def handle_input(self, pin):
        return GPIO.input(pin)

    def open_gate(self) -> bool:
        Hardware.servo_pwm.ChangeDutyCycle(1.9)
        return False

    def close_gate(self) -> bool:
        Hardware.servo_pwm.ChangeDutyCycle(9.8)
        return True

    def cleanup(self):
        Hardware.servo_pwm.stop()
        GPIO.cleanup()
        return None

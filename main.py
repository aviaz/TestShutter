import time
import datetime
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

# time interval for normal button presses
BUTTON_HOLD = 2  # seconds
BUTTON_TIMEOUT = 0.2  # seconds


# action on pin
def switch_pin(pin_nr, is_open):
    try:
        if is_open:
            # Pin ON
            # to turn a button on we just need to set the GPIO to output
            # it will then output low level, which equals a button press
            print("pin {}: ON".format(pin_nr))
            GPIO.setup(pin_nr, GPIO.OUT)
        else:
            # Pin OFF
            # accordingly, to turn a button of we configure the GPIO to input
            # the high impetance state equals no button press
            print("pin {}: OFF".format(pin_nr))
            GPIO.setup(pin_nr, GPIO.IN)

        # delay
        time.sleep(BUTTON_TIMEOUT)
    except RuntimeError as ex:
        print("Error controlling GPIOs: " + str(ex))


# control shutters
def shutter_action(direction, is_open):
    if direction == "up":
        switch_pin(17, is_open)
    else:
        switch_pin(27, is_open)


def shutter_up():
    print("Going up...")
    shutter_action("up")


def shutter_down():
    print("And back down...")
    shutter_action("down")


time.sleep(2)
shutter_action("up", True)
time.sleep(20)
shutter_action("up", False)
shutter_action("down", True)
time.sleep(30)
shutter_action("down", False)

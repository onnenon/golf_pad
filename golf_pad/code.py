import time
from enum import Enum

import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from digitalio import DigitalInOut, Direction, Pull

# Turn the LED on
led = DigitalInOut(board.LED)
led.direction = Direction.OUTPUT
led.value = True

kbd = Keyboard(usb_hid.devices)

pins = [
    board.GP0,
    board.GP1,
    board.GP2,
    board.GP3,
    board.GP4,
]

keymap = [Keycode.A, Keycode.B, Keycode.C, Keycode.D, Keycode.E]


class Switch_State(Enum):
    ON = 1
    OFF = 0


class Switch:
    def __init__(self, pin, keycode):
        self.dio = get_dio_for_pin(pin)
        self.state = Switch_State.ON
        self.keycode = keycode

    def value(self):
        return self.dio.value

    def toggle_state(self):
        self.state = self.state + 1 % 2


def get_dio_for_pin(pin):
    dio = DigitalInOut(pin)
    dio.direction = Direction.INPUT
    dio.pull = Pull.UP
    return dio


switches = [Switch(pin, keymap[index]) for index, pin in enumerate(pins)]

while True:
    for switch in switches:
        try:
            if switch.state == Switch_State.ON:
                if not switch.value:
                    kbd.press(switch.keycode)
            else:
                if switch.value:
                    kbd.release(switch.keycode)
        except ValueError:
            pass
        switch.toggle_state()
    time.sleep(0.01)

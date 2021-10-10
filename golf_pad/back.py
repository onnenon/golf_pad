import time

import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from digitalio import DigitalInOut, Direction, Pull

print("---Pico Pad Keyboard---")

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

switches = [0] * len(pins)

for index, pin in enumerate(pins):
    switches[index] = DigitalInOut(pin)
    switches[index].direction = Direction.INPUT
    switches[index].pull = Pull.UP

switch_state = [0] * len(pins)

while True:
    for index, state in enumerate(switch_state):
        try:
            if state == 0:
                if not switches[index].value:
                    kbd.press(keymap[index])
                switch_state[index] = 1
            else:
                if switches[index].value:
                    kbd.release(keymap[index])
                switch_state[index] = 0
        except ValueError:
            pass
    time.sleep(0.01)

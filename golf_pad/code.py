import board
import keypad
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from digitalio import DigitalInOut, Direction

keymap = [
    Keycode.A,
    Keycode.B,
    Keycode.C,
    Keycode.D,
    Keycode.E,
    Keycode.F,
    Keycode.G,
    Keycode.H,
    Keycode.I,
    Keycode.J,
    Keycode.K,
    Keycode.L,
]

pins = [
    board.GP0,
    board.GP1,
    board.GP2,
    board.GP3,
    board.GP4,
    board.GP5,
    board.GP6,
    board.GP7,
    board.GP8,
    board.GP9,
    board.GP10,
    board.GP11,
]

led = DigitalInOut(board.LED)
led.direction = Direction.OUTPUT
led.value = True

keyboard = Keyboard(usb_hid.devices)

switches = keypad.Keys(pins, value_when_pressed=False, pull=True)

while True:
    if event := switches.events.get():
        if event.pressed:
            keyboard.press(keymap[event.key_number])
        else:
            keyboard.release(keymap[event.key_number])

import board
import keypad
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from digitalio import DigitalInOut, Direction

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

switches = keypad.Keys(pins, value_when_pressed=False, pull=True)

while True:
    event = switches.events.get()
    if event:
        if event.pressed:
            kbd.press(keymap[event.key_number])
        if event.released:
            kbd.release(keymap[event.key_number])

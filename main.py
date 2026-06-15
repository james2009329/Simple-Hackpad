import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode
import rotaryio
import digitalio
import time

kbd = Keyboard(usb_hid.devices)
cc = ConsumerControl(usb_hid.devices)

# Buttons
sw1 = digitalio.DigitalInOut(board.D10)  # Cut
sw2 = digitalio.DigitalInOut(board.D9)   # Copy
sw3 = digitalio.DigitalInOut(board.D8)   # Paste
for sw in [sw1, sw2, sw3]:
    sw.direction = digitalio.Direction.INPUT
    sw.pull = digitalio.Pull.UP

# Encoder
encoder = rotaryio.IncrementalEncoder(board.D0, board.D1)
enc_btn = digitalio.DigitalInOut(board.D2)
enc_btn.direction = digitalio.Direction.INPUT
enc_btn.pull = digitalio.Pull.UP

last_position = encoder.position
last_sw1 = last_sw2 = last_sw3 = last_enc_btn = True

while True:
    if not sw1.value and last_sw1:
        kbd.send(Keycode.CONTROL, Keycode.X)  # Cut
    last_sw1 = sw1.value

    if not sw2.value and last_sw2:
        kbd.send(Keycode.CONTROL, Keycode.C)  # Copy
    last_sw2 = sw2.value

    if not sw3.value and last_sw3:
        kbd.send(Keycode.CONTROL, Keycode.V)  # Paste
    last_sw3 = sw3.value

    position = encoder.position
    if position > last_position:
        cc.send(ConsumerControlCode.VOLUME_INCREMENT)
    elif position < last_position:
        cc.send(ConsumerControlCode.VOLUME_DECREMENT)
    last_position = position

    if not enc_btn.value and last_enc_btn:
        cc.send(ConsumerControlCode.PLAY_PAUSE)
    last_enc_btn = enc_btn.value

    time.sleep(0.01)

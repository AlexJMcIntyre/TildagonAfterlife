#Simple rainbow demo script

import machine
import neopixel
import time

LED_PIN = 10
NUM_LEDS = 18

leds = neopixel.NeoPixel(
    machine.Pin(LED_PIN),
    NUM_LEDS
)


def wheel(position):
    """Convert 0-255 colour wheel position to RGB."""

    position %= 256

    if position < 85:
        return (
            position * 3,
            255 - position * 3,
            0
        )

    if position < 170:
        position -= 85
        return (
            255 - position * 3,
            0,
            position * 3
        )

    position -= 170

    return (
        0,
        position * 3,
        255 - position * 3
    )


# Position of every physical LED around the dial.
#
# Front:
#   0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
#
# Back:
#   1.5, 3.5, 5.5, 7.5, 9.5, 11.5

led_positions = []

for i in range(12):
    led_positions.append(i)

for i in range(6):
    led_positions.append(i * 2 + 1.5)


offset = 0

while True:

    for led in range(NUM_LEDS):

        position = led_positions[led]

        leds[led] = wheel(
            int(position * 256 / 12) + offset
        )

    leds.write()

    offset = (offset + 1) % 256

    time.sleep(0.02)
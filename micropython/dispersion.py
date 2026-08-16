import machine
import neopixel
import time

# One white point splits into a spectrum of colours.
# Slight differences in particle speed cause the spectrum
# to drift and interfere, and it looks like chaos at first but
# if you keep watching, patterns and nodes start reforming out
# of the noise. 

# settings

LED_PIN = 10
NUM_LEDS = 18
FRONT_LEDS = 12

PARTICLES = 12

# How quickly the spectrum moves.
BASE_SPEED = 0.005

# How much the particles differ in speed.
SPEED_SPREAD = 1 / 2400

# How far each particle illuminates neighbouring LEDs.
PARTICLE_SPREAD = 0.75

# Frame delay. Lower = faster / smoother.
FRAME_DELAY = 0.01

# Maximum brightness of each colour component.
COLOUR_LEVEL = 85



# hardware

leds = neopixel.NeoPixel(
    machine.Pin(LED_PIN),
    NUM_LEDS
)



# Spectrum

# The colours are evenly distributed around the RGB colour
# wheel. Because they all start in the same place, they begin
# as white and gradually separate into a spectrum.

SPECTRUM = [
    [COLOUR_LEVEL,  0,              0],
    [COLOUR_LEVEL,  COLOUR_LEVEL//2, 0],
    [COLOUR_LEVEL,  COLOUR_LEVEL,   0],
    [COLOUR_LEVEL//2, COLOUR_LEVEL, 0],
    [0,              COLOUR_LEVEL,  0],
    [0,              COLOUR_LEVEL,  COLOUR_LEVEL//2],
    [0,              COLOUR_LEVEL,  COLOUR_LEVEL],
    [0,              COLOUR_LEVEL//2, COLOUR_LEVEL],
    [0,              0,              COLOUR_LEVEL],
    [COLOUR_LEVEL//2, 0,             COLOUR_LEVEL],
    [COLOUR_LEVEL,   0,              COLOUR_LEVEL],
    [COLOUR_LEVEL,   0,              COLOUR_LEVEL//2],
]



# particle


class Particle:

    def __init__(self, position, colour, speed, spread):
        self.position = position
        self.colour = colour
        self.speed = speed
        self.spread = spread


# Create the spectrum

particles = []

for i in range(PARTICLES):

    speed = BASE_SPEED + i * SPEED_SPREAD

    particles.append(
        Particle(
            position=0,
            colour=SPECTRUM[i],
            speed=speed,
            spread=PARTICLE_SPREAD
        )
    )



# Main loop

while True:

    # Draw the particles onto the LEDs

    for led in range(FRONT_LEDS):

        red = 0
        green = 0
        blue = 0

        for particle in particles:

            # Distance around the circular LED arrangement
            distance = abs(particle.position - led)
            distance = min(
                distance,
                FRONT_LEDS - distance
            )

            # Does this particle illuminate this LED?
            if distance <= particle.spread:

                brightness = (
                    1.0 -
                    distance / particle.spread
                )

                red += particle.colour[0] * brightness
                green += particle.colour[1] * brightness
                blue += particle.colour[2] * brightness



        # Normalise the colour if it is brighter than the LEDs can display.
        # This preserves the colour balance rather than simply clipping individual RGB channels.


        maximum = max(red, green, blue)

        if maximum > 255:

            scale = 255 / maximum

            red *= scale
            green *= scale
            blue *= scale


        leds[led] = (
            int(red),
            int(green),
            int(blue)
        )



    # Move the spectrum

    for particle in particles:

        particle.position += particle.speed

        # Wrap around the circular display
        particle.position %= FRONT_LEDS


    # Update the LEDs

    leds.write()

    time.sleep(FRAME_DELAY)
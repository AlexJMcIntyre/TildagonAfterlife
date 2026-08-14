import machine
import neopixel
import time

LED_PIN = 10
NUM_LEDS = 18 #12 leds on the front, 6 on the rear

leds = neopixel.NeoPixel(
    machine.Pin(LED_PIN),
    NUM_LEDS
)

while True:
    for i in range(NUM_LEDS):
        leds[i] = [255,0,0] # red only
    leds.write()

    time.sleep(2) # 2 second wait
    
    for i in range(NUM_LEDS):
        leds[i] = [0,255,0] # green only
    leds.write()

    time.sleep(2) # 2 second wait
        
    for i in range(NUM_LEDS):
        leds[i] = [0,0,255] # blue only
    leds.write()

    time.sleep(2) # 2 second wait
        
    for i in range(NUM_LEDS):
        leds[i] = [100,100,100] # combine all colours for white
    leds.write()

    time.sleep(2) # 2 second wait
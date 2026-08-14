from machine import Pin
from time import sleep

# Button GPIO mappings 
BUTTON_PINS = {
    "BTN_A": 4,
    "BTN_B": 5,
    "BTN_C": 20,
    "BTN_D": 21,
    "BTN_E": 2,
    "BTN_F": 0
}

# Initialize buttons with internal pull-ups (Active LOW when pressed)
buttons = {}
for name, pin_num in BUTTON_PINS.items():
    buttons[name] = Pin(pin_num, Pin.IN, Pin.PULL_UP)

print("BUTTON TEST READY")
while True:
    # Check active buttons
    for btn_name, pin in buttons.items():
        if pin.value() == 0:  # 0 = Pressed
            print(btn_name, " pressed ")
    sleep(0.05)  # Small delay between polls
       
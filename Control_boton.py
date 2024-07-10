from machine import Pin
import utime

led = Pin(2, Pin.OUT)
key = Pin(4, Pin.IN, Pin.PULL_UP)

def led_on():
    led.value(1)

def led_off():
    led.value(0)

def press_state():
    if key.value() == 0:
        return True
    return False 

while True:
    if press_state() == True:
        print("press")
        led_on()
    else:
        led_off()
    utime.sleep(0.1)

from machine import Pin
import time

trig = Pin(2, Pin.OUT)
echo = Pin(4, Pin.IN)

while True:
    trig.value(0)
    time.sleep(0.1)
    trig.value(1)
    time.sleep_us(2)
    trig.value(0)
    while echo.value()==0:
        pulse_start = time.ticks_us()
    while echo.value()==1:
        pulse_end = time.ticks_us()
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 0.0343 / 2
    distance = round(distance, 2)
    print ('Distancia:',"{:.2f}".format(distance),'cm')
    time.sleep(1)

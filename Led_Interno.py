import machine
import time

# Configura el pin del LED interno (GPIO 2 en el ESP32)
led = machine.Pin(2, machine.Pin.OUT)

# Enciende el LED durante 5 segundos
led.on()
time.sleep(5)
led.off()
# Hace que el LED parpadee durante 5 segundos
for _ in range(10):
    led.on()
    time.sleep(0.5)
    led.off()
    time.sleep(0.5)

# Enciende el LED durante otros 5 segundos
led.on()
time.sleep(5)
led.off()
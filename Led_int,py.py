import machine
import time

# Configura el número de pin para el LED interno (puede variar según la placa)
led_pin_number = 2

# Configura el pin como salida
led_pin = machine.Pin(led_pin_number, machine.Pin.OUT)

# Enciende el LED
led_pin.on()

# Espera unos segundos
time.sleep(5)

# Apaga el LED
led_pin.off()
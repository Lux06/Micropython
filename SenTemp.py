import machine
from machine import Pin, SoftI2C
from lcd_api import LcdApi
from i2c_lcd import I2cLcd
from time import sleep
import RF433
import time

# Configuración de los pines
receive_pin = 16

# Inicialización del pin de recepción
rx = Pin(receive_pin, Pin.IN)

def receive_data():
    data = []
    start_time = time.ticks_us()
    while time.ticks_diff(time.ticks_us(), start_time) < 10000:  # Espera 10 ms
        while rx.value() == 1:
            pass
        pulse_start = time.ticks_us()
        while rx.value() == 0:
            pass
        pulse_duration = time.ticks_diff(time.ticks_us(), pulse_start)
        data.append(1 if pulse_duration > 1000 else 0)
    return data

def bits_to_bytes(bits):
    bytes_list = [bits[i:i+8] for i in range(0, len(bits), 8)]
    byte_data = bytearray()
    for byte_bits in bytes_list:
        byte_value = 0
        for bit in byte_bits:
            byte_value = (byte_value << 1) | bit
        byte_data.append(byte_value)
    return byte_data

I2C_ADDR = 0x27
totalRows = 2
totalColumns = 16

# I2C for ESP32
i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=10000)
lcd = I2cLcd(i2c, I2C_ADDR, totalRows, totalColumns)

# Función para mostrar los datos de temperatura y humedad en la pantalla LCD
def mostrar_datos(temp, humedad):
    lcd.clear()
    lcd.putstr("Temp:{} C\n".format(temp))
    lcd.putstr("Humedad:{} %".format(humedad))

while True:
    try:
        print("eNTRA2")
        # Recibir un dato
        received_bits = receive_data()
    
        if received_bits:
            decoded_data = bits_to_bytes(received_bits)
            print("Recibido:", decoded_data)
        # Esperar antes de recibir el siguiente dato
        time.sleep(2)
        # Simula la recepción de datos de temperatura y humedad desde el receptor RF 433MHz
        # Aquí debes implementar la lógica para recibir los datos correctamente
        received_temp = 25  # Ejemplo de temperatura recibida
        received_humidity = 60  # Ejemplo de humedad recibida
        
        # Muestra los datos en la pantalla LCD
        mostrar_datos(received_temp, received_humidity)
    except Exception as e:
        # En caso de error al recibir los datos
        lcd.clear()
        lcd.putstr("Error de recepción")
        print("Error de recepción:", e)
    
    sleep(2)

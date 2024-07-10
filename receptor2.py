from machine import Pin, UART
from time import sleep

# Configuración del pin del receptor RF
receive_pin = 16  # Asegúrate de conectar el receptor RF a este pin
rx = Pin(receive_pin, Pin.IN)

# Configuración del módulo UART para la comunicación serie
uart = UART(1, baudrate=9600, rx=receive_pin)

while True:
    try:
        received_data = uart.read(8)  # Lee hasta 12 bytes
        if received_data:
            received_text = received_data.decode('utf-8')
            print("Datos recibidos:", received_text)
       
    except Exception as e:
        print("Error:", e)
   
    sleep(0.5)
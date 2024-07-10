from machine import Pin, UART, PWM, ADC
import time
import random
from utime import sleep

command = ''
str(command)

#Puente H
m11 = PWM(Pin(32))
m11.freq(1500)
m12 = PWM(Pin(33))
m12.freq(1500)
m21 = PWM(Pin(25))
m21.freq(1500)
m22 = PWM(Pin(26))
m22.freq(1500)

#Funcion para el puente H
def my_map(x, in_min, in_max, out_min, out_max):
    return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

#uart = UART(1, 9600)
uart = UART(1, baudrate=9600, rx=16, tx=17)

# Configura el pin del sensor infrarrojo
ir_tracker_pinCD1 = ADC(Pin(15))

while True:
    # Lee el valor analógico del sensor infrarrojo
    ir_value = ir_tracker_pinCD1.read()
    # Estima la distancia basada en la lectura del sensor 
    distancia_estimada = (1023 - ir_value) / 10  

    print("Valor del sensor IR Tracker:", ir_value)
    print("Distancia estimada:", distancia_estimada, "cm")

    #time.sleep(1)
    
    #Seguidor de pelota velocidad
    pulse = my_map(100, 0, 100, 0, 65535)
    #pulse = my_map(100, 0, 100, 0, 65535)
    if uart.any():
        command = uart.readline()
        print(command)
   
    if 'F' in command:
        m11.duty_u16(0)
        m12.duty_u16(0)
        m21.duty_u16(0)
        m22.duty_u16(0)
        m12.duty_u16(pulse)
        m21.duty_u16(pulse)
        
    elif "B" in command:
        m11.duty_u16(0)
        m12.duty_u16(0)
        m21.duty_u16(0)
        m22.duty_u16(0)
        m11.duty_u16(pulse)
        m22.duty_u16(pulse)
      
    elif "L" in command:
        m11.duty_u16(0)
        m12.duty_u16(0)
        m21.duty_u16(0)
        m22.duty_u16(0)
        m21.duty_u16(pulse)
        m11.duty_u16(pulse)
        
    elif "R" in command:
        m11.duty_u16(0)
        m12.duty_u16(0)
        m21.duty_u16(0)
        m22.duty_u16(0)
        m12.duty_u16(pulse)
        m22.duty_u16(pulse)
        
    else:
        m11.duty_u16(0)
        m12.duty_u16(0)
        m21.duty_u16(0)
        m22.duty_u16(0)
        

from machine import Pin, UART
import utime

# Configurar UART para la ESP32
uart0 = UART(1, baudrate=9600, rx=16, tx=17)  # Cambiar los números de pin según tu configuración
LED = Pin(2, Pin.OUT)
LED.value(0)

def Resp(uart=uart0, timeout=2000):
    prvMills = utime.ticks_ms()
    resp = b""
    while (utime.ticks_ms() - prvMills) < timeout:
        if uart.any():
            resp = b"".join([resp, uart.read(1)])
    print("resp:")
    try:
        return resp.decode()
    except UnicodeError:
        return resp

while True:
    word = Resp(uart0)
    print(word)
    if word.find("L1") != -1:
        LED.value(1)
        uart0.write("PRENDIDO\r\n")
    elif word.find("L2") != -1:
        LED.value(0)
        uart0.write("APAGADO\r\n")
import socket
import network
from lcd_api import LcdApi
from i2c_lcd import I2cLcd
import machine
from machine import Pin, SoftI2C
from time import sleep
import time

I2C_ADDR = 0x27
totalRows = 2
totalColumns = 16

# I2C for ESP32
i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=10000)
lcd = I2cLcd(i2c, I2C_ADDR, totalRows, totalColumns)

# Configuración de la red WiFi
wifi_ssid = 'OLAX_MFi_2A94'
wifi_password = '36138516'

#local_ip = '192.168.0.101'
# Nueva configuración de red
new_ip = "192.168.0.150"
new_subnet = "255.255.255.0"
new_gateway = "192.168.0.1"
new_dns = "8.8.8.8"


# Dirección IP y puerto de esta placa (Placa B)
server_ip = '192.168.0.100'
server_port = 80  # Puerto de tu elección

# Conexión WiFi
wifi = network.WLAN(network.STA_IF)
# Cambiar la configuración utilizando ifconfig()
wifi.ifconfig((new_ip, new_subnet, new_gateway, new_dns))

# Imprimir la nueva configuración
ip, subnet, gateway, dns = wifi.ifconfig()
print("Nueva IP:", ip)
print("Nueva Subnet:", subnet)
print("Nuevo Gateway:", gateway)
print("Nuevo DNS:", dns)

wifi.active(True)
wifi.connect(wifi_ssid, wifi_password)
while not wifi.isconnected():
    pass

# Crear socket y enlazar
sock = socket.socket()
sock.bind((ip, server_port))
sock.listen(1)
    
print("Esperando conexión...")
client, addr = sock.accept()
print("Conexión establecida desde:", addr)

# Función para mostrar los datos de temperatura y humedad en la pantalla LCD
def mostrar_datos(temp, humedad, alt):
    lcd.clear()
    lcd.putstr("Temp:{} C\n".format(temp))
    lcd.putstr("Humedad:{} %".format(humedad))
    lcd.putstr("Alt:{}".format(alt))

while True:
    # Recibir datos
    datos_recibidos = client.recv(1024).decode()
    print("Datos recibidos:", datos_recibidos)
    dat=datos_recibidos.split(',')
    #print(dat)
    received_temp = dat[0]  # Ejemplo de temperatura recibida
    received_humidity = dat[1] # Ejemplo de humedad recibida
    received_alt = dat[2]
    
    # Muestra los datos en la pantalla LCD
    mostrar_datos(received_temp, received_humidity, received_alt)

    # Cerrar socket
    #client.close()
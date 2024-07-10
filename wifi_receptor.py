import socket
import network
import machine

# Configuración de la red WiFi
wifi_ssid = 'OLAX_MFi_2A94'
wifi_password = '36138516'

# Nueva configuración de red
new_ip = "192.168.0.145"
new_subnet = "255.255.255.0"
new_gateway = "192.168.0.1"
new_dns = "8.8.8.8"

#Configurar puerto
server_port = 80  # Puerto de tu elección

# Conexión WiFi
wifi = network.WLAN(network.STA_IF)
# Cambiar la configuración utilizando ifconfig()
wifi.ifconfig((new_ip, new_subnet, new_gateway, new_dns))

# Imprimir la nueva configuración
ip, subnet, gateway, dns = wifi.ifconfig()
print("Nueva IP:", ip)

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

#Mostrar los datos recibidos
datos_recibidos = client.recv(1024).decode()
print("Datos recibidos:", datos_recibidos)

# Cerrar socket
client.close()

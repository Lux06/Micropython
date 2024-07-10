import network
import socket

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)

SSID = 'OLAX_MFi_2A94'
PASSWORD = '36138516'

sta_if.connect(SSID, PASSWORD)

while not sta_if.isconnected():
    pass

print('Conexión WiFi establecida con', sta_if.ifconfig()[0])
#print('IP:', sta_if.ifconfig()[0])

PORT = 8080 

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_socket.bind(('0.0.0.0', PORT))

print(f"Esperando conexiones en {sta_if.ifconfig()[0]}:{PORT}...")

while True:
    try:
        data, client_address = server_socket.recvfrom(1024)
        print(f"Datos recibidos de {client_address}: {data.decode('utf-8')}")

    except Exception as e:
        print(f"Error de conexión: {str(e)}")

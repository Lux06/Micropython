from machine import Pin, UART
import utime
import time

# Inicializa la comunicación UART con el módulo GPS
gpsModule = UART(1, baudrate=9600, rx=16, tx=17)

# Define algunas variables globales para almacenar datos del GPS
FIX_STATUS = False
TIMEOUT = False
latitude = ""
longitude = ""
satellites = ""
GPStime = ""

def getGPS(gpsModule):
    global FIX_STATUS, TIMEOUT, latitude, longitude, satellites, GPStime
    timeout = time.time() + 8  # Establece un límite de tiempo para la adquisición de datos
    while True:
        gpsModule.readline()  # Descarta la primera línea
        buff = str(gpsModule.readline())  # Lee una línea del módulo GPS
        parts = buff.split(',')  # Divide la línea en partes utilizando ',' como separador

        if parts[0] == "b'$GPGGA" and len(parts) >= 7:
            print(buff)  # Imprime la línea GPGGA
            GPStime = parts[1][0:2] + ":" + parts[1][2:4] + ":" + parts[1][4:6]
            
            # Extrae y convierte la latitud y longitud
            latitude = float(convertToDegree(parts[2]))
            if parts[3] == 'S':
                latitude = -latitude
            longitude = float(convertToDegree(parts[4]))
            if parts[5] == 'W':
                longitude = -longitude
            satellites = parts[7]
            FIX_STATUS = True  # Indica que se ha obtenido una fijación GPS
            break

        if time.time() > timeout:
            TIMEOUT = True  # Indica que se ha superado el límite de tiempo
            break
        utime.sleep_ms(500)  # Espera 500 ms antes de volver a intentar

def convertToDegree(RawDegrees):
    RawAsFloat = float(RawDegrees)
    firstdigits = int(RawAsFloat / 100)
    nexttwodigits = RawAsFloat - float(firstdigits * 100)
    Converted = float(firstdigits + nexttwodigits / 60.0)
    Converted = '{0:.6f}'.format(Converted)
    return str(Converted)

# Bucle principal
while True:
    getGPS(gpsModule)
    
    if FIX_STATUS:
        print("Printing GPS data...")
        print("Latitude: " + str(latitude))
        print("Longitude: " + str(longitude))
        print("Satellites: " + str(satellites))
        print("Time: " + GPStime)
        print("----------------------")
        FIX_STATUS = False

    if TIMEOUT:
        print("No GPS data is found.")
        TIMEOUT = False
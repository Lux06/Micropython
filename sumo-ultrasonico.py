from machine import Pin, PWM, ADC
import time
import _thread

# Definimos los pines para los motores
left_motor_forward = Pin(33, Pin.OUT)  # m11
left_motor_backward = Pin(32, Pin.OUT)  # m12
right_motor_forward = Pin(25, Pin.OUT)  # m21
right_motor_backward = Pin(26, Pin.OUT)  # m22

# Definimos los pines para los sensores de seguimiento
left_tracker = ADC(Pin(36))
right_tracker = ADC(Pin(39))

# Inicializamos el sensor ultrasónico
trig_pins = [Pin(2, Pin.OUT), Pin(14, Pin.OUT), Pin(13, Pin.OUT)]  # Pines de disparo para los tres sensores
echo_pins = [Pin(4, Pin.IN), Pin(34, Pin.IN), Pin(12, Pin.IN)] 

# Función personalizada para medir la duración del pulso
def measure_pulse(pin, level, timeout=100000):
    start = time.ticks_us()
    while pin.value() != level:
        if time.ticks_diff(time.ticks_us(), start) > timeout:
            return -1
    start = time.ticks_us()
    while pin.value() == level:
        if time.ticks_diff(time.ticks_us(), start) > timeout:
            return -1
    return time.ticks_diff(time.ticks_us(), start)

# Función para medir distancia con el sensor ultrasónico
def measure_distance(trig_pin, echo_pin):
    trig_pin.on()
    time.sleep_us(10)
    trig_pin.off()
    pulse_duration = measure_pulse(echo_pin, 1)
    if pulse_duration < 0:
        return -1
    distance = (pulse_duration * 0.0343) / 2
    return distance

# Funciones para controlar los motores
def move_forward():
    left_motor_forward.on()
    left_motor_backward.off()
    right_motor_forward.on()
    right_motor_backward.off()

def move_backward():
    left_motor_forward.off()
    left_motor_backward.on()
    right_motor_forward.off()
    right_motor_backward.on()

def turn_left(degrees=5):
    left_motor_forward.off()
    left_motor_backward.on()
    right_motor_forward.on()
    right_motor_backward.off()
    time.sleep(degrees / 90)  # Ajusta este valor según la velocidad de tu robot
    stop()

def turn_right(degrees=5):
    left_motor_forward.on()
    left_motor_backward.off()
    right_motor_forward.off()
    right_motor_backward.on()
    time.sleep(degrees / 90)  # Ajusta este valor según la velocidad de tu robot
    stop()

def stop():
    left_motor_forward.off()
    left_motor_backward.off()
    right_motor_forward.off()
    right_motor_backward.off()

def backup_and_turn():
    move_backward()
    time.sleep(0.2)  # Retrocede por 0.2 segundos
    stop()
    time.sleep(0.1)  # Pequeña pausa
    turn_left(30)  # Gira a la izquierda por 30 grados
    stop()

# Función para manejar los sensores ultrasónicos en un hilo
def ultrasonic_thread():
    global distances
    while True:
        distances = [measure_distance(trig_pins[i], echo_pins[i]) for i in range(3)]
        time.sleep_ms(50)  # Tiempo de espera reducido para mayor velocidad

# Función para manejar el movimiento de los motores y los sensores infrarrojos en un hilo
def motor_thread():
    while True:
        left_tracker_value = left_tracker.read()
        right_tracker_value = right_tracker.read()
        
        # Interpretación de los valores de los sensores de seguimiento
        left_on_white = left_tracker_value >= 4000
        right_on_white = right_tracker_value >= 4000

        if left_on_white or right_on_white:  # Detecta la línea blanca
            backup_and_turn()
        else:
            # Evaluación de las distancias medidas por los sensores ultrasónicos
            if distances[0] < 35 and distances[0] > 0:  # Obstáculo cercano en el sensor frontal
                move_forward()
            elif distances[1] < 35 and distances[1] > 0:  # Obstáculo cercano en el sensor izquierdo
                turn_left(10)
            elif distances[2] < 35 and distances[2] > 0:  # Obstáculo cercano en el sensor derecho
                turn_right(10)
            else:
                move_forward()
        
        time.sleep_ms(50)  # Tiempo de espera reducido para mayor velocidad

# Iniciamos los hilos
distances = [0, 0, 0]
_thread.start_new_thread(ultrasonic_thread, ())
_thread.start_new_thread(motor_thread, ())

# Mantenemos el hilo principal corriendo
while True:
    time.sleep(1)

from machine import Pin
import time

# Definimos los pines para los motores
left_motor_forward = Pin(33, Pin.OUT)
left_motor_backward = Pin(32, Pin.OUT)
right_motor_forward = Pin(25, Pin.OUT)
right_motor_backward = Pin(26, Pin.OUT)

# Funciones para controlar los motores
def test_left_motor_forward():
    print("Probando motor izquierdo hacia adelante")
    left_motor_forward.on()
    time.sleep(2)
    left_motor_forward.off()

def test_left_motor_backward():
    print("Probando motor izquierdo hacia atrás")
    left_motor_backward.on()
    time.sleep(2)
    left_motor_backward.off()

def test_right_motor_forward():
    print("Probando motor derecho hacia adelante")
    right_motor_forward.on()
    time.sleep(2)
    right_motor_forward.off()

def test_right_motor_backward():
    print("Probando motor derecho hacia atrás")
    right_motor_backward.on()
    time.sleep(2)
    right_motor_backward.off()

def stop_all_motors():
    print("Deteniendo todos los motores")
    left_motor_forward.off()
    left_motor_backward.off()
    right_motor_forward.off()
    right_motor_backward.off()

# Función principal de prueba
def test_motors():
    stop_all_motors()
    time.sleep(1)
    test_left_motor_forward()
    time.sleep(1)
    test_left_motor_backward()
    time.sleep(1)
    test_right_motor_forward()
    time.sleep(1)
    test_right_motor_backward()
    time.sleep(1)
    stop_all_motors()

# Ejecutamos la prueba de los motores
test_motors()

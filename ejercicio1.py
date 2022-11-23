#------------------------------
#Ejercicio: Práctica p4 sensores y actuadores --> 
#Autores: Jorge Martín y Rebeca Sánchez
#Fecha límite de entrega: 23/11/22
#Objetivo: obtener la velocidad angular (rpm) del encoder
#------------------------------

import time
import signal
import sys
import RPi.GPIO as GPIO

OPTOINTERRUPTOR= 15
BOUNCETIME= 100
n=0
MUESCAS= 10
TIME=2
contador = 0
rpm = 0


def callbackContador(canal):
    global n
    n=n+1

def print_rpm(contador):
    print(contador*60/MUESCAS/TIME, "revoluciones por minuto (rpm)")
    time.sleep(TIME)

    
if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    #Establecer encoder
    GPIO.setup(OPTOINTERRUPTOR, GPIO.IN, pull_up_down=GPIO.PUD_UP)    
    GPIO.setwarnings(False)
    n=0
    GPIO.add_event_detect(OPTOINTERRUPTOR, GPIO.FALLING,callback=callbackContador, bouncetime = BOUNCETIME)
    while True:
        contador = n
        n=0
        print_rpm(contador)
        
def callbackSalir(senial,cuadro):
    GPIO.cleanup()
    sys.exit(0)
        
if __name__=="__main__":
     main()

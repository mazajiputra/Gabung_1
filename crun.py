#persiapan
import RPi.GPIO as GPIO
from time import sleep
import jalan_raw
import cmultiplexer_raw

# The script as below using BCM GPIO 00..nn numbers
GPIO.setmode(GPIO.BCM)

# Disable Warnings
GPIO.setwarnings(False)


#Jalan

# Set relay pins as output
GPIO.setup(12, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)

#Matikan dulu
GPIO.output(12, GPIO.HIGH)
GPIO.output(16, GPIO.HIGH)
GPIO.output(20, GPIO.HIGH)
GPIO.output(21, GPIO.HIGH)   
sleep(2) 


def f1():
    try:
        #ganti relay dan baca
        GPIO.output(12, GPIO.LOW)
        GPIO.output(16, GPIO.HIGH)
        GPIO.output(20, GPIO.HIGH)
        GPIO.output(21, GPIO.HIGH)
        #Ganti channel
        cmultiplexer_raw.cetak(2)
        sleep(0.5)
        jalan_raw.cetak()
        sleep(0.5)
        jalan_raw.cetak()
        sleep(3) 
    except Exception as e:
        print('Error:',e)

def f2():
    try:
        #ganti relay dan baca
        GPIO.output(12, GPIO.HIGH)
        GPIO.output(16, GPIO.LOW)
        GPIO.output(20, GPIO.HIGH)
        GPIO.output(21, GPIO.HIGH)
        #Ganti channel
        cmultiplexer_raw.cetak(4)
        sleep(0.5)
        jalan_raw.cetak()
        sleep(0.5)
        jalan_raw.cetak()
        sleep(3) 
        # Turn all relays OFF
    except Exception as e:
        print('Error:',e)

def f3():
    try:
        #ganti relay dan baca
        GPIO.output(12, GPIO.HIGH)
        GPIO.output(16, GPIO.HIGH)
        GPIO.output(20, GPIO.LOW)
        GPIO.output(21, GPIO.HIGH)
        #Ganti channel
        cmultiplexer_raw.cetak(5)
        sleep(0.5)
        jalan_raw.cetak()
        sleep(0.5)
        jalan_raw.cetak()
        sleep(3) 
    except Exception as e:
        print('Error:',e)
def f4():
    try:
        #ganti relay dan baca
        GPIO.output(12, GPIO.HIGH)
        GPIO.output(16, GPIO.HIGH)
        GPIO.output(20, GPIO.HIGH)
        GPIO.output(21, GPIO.LOW)
        #Ganti channel
        cmultiplexer_raw.cetak(7)
        sleep(0.5)
        jalan_raw.cetak()
        sleep(0.5)
        jalan_raw.cetak()
        sleep(3) 
    except Exception as e:
        print('Error:',e)
while (True):
        #1
        f1()
        #2
        f2()
        #3
        f3()
        #4
        f4()
def selesai():
# catches the ctrl-c command, breaks the loop above 
# and turns the relays off
    GPIO.output(12, GPIO.HIGH)
    GPIO.output(16, GPIO.HIGH)
    GPIO.output(20, GPIO.HIGH)
    GPIO.output(21, GPIO.HIGH)   
    #Sleep for 5 seconds
    # sleep(5)
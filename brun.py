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

def jalan():
    
        #1
        # Turn all relays ON
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
        # Turn all relays OFF
        #2
        # Turn all relays ON
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
        #3
        # Turn all relays ON
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
        # Turn all relays OFF
        #4
                # Turn all relays ON
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
        # Turn all relays OFF
try:
    jalan()

except RuntimeError:
    #aise ImportError(e)
    jalan()
except KeyboardInterrupt:
# catches the ctrl-c command, breaks the loop above 
# and turns the relays off
    GPIO.output(12, GPIO.HIGH)
    GPIO.output(16, GPIO.HIGH)
    GPIO.output(20, GPIO.HIGH)
    GPIO.output(21, GPIO.HIGH)   
    #Sleep for 5 seconds
    # sleep(5)
except:
    jalan()
print("Program selesai")
import time
import board
import adafruit_shtc3




#while True:
def cetak():
    i2c = board.I2C()   # uses board.SCL and board.SDA
    sht = adafruit_shtc3.SHTC3(i2c)
    temperature, relative_humidity = sht.measurements
    # print("Temperature: %0.1f C" % temperature)
    # print("Humidity: %0.1f %%" % relative_humidity)
    print(temperature)
    print(relative_humidity)
    print("")
    time.sleep(1)
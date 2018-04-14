import OPi.GPIO as gpio

import dht11
import time
import datetime


gpio.setmode(gpio.BOARD)
PIN2 = 5

instance = dht11.DHT11(pin=PIN2)

while True:
    result = instance.read()
    if result.is_valid():
        print("Last valid input: " + str(datetime.datetime.now()))
        print("Temperature: %d C" % result.temperature)
        print("Humidity: %d %%" % result.humidity)

    time.sleep(1)

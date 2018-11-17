import os
import time
import datetime
import glob
from time import strftime
from Adafruit_BME280 import *
import csv

sensor = BME280(t_mode=BME280_OSAMPLE_8, p_mode=BME280_OSAMPLE_8, h_mode=BME280_OSAMPLE_8)

def get_data():
    secs = float(time.time()) * 1000

    temperature = float('{0:.1f}'.format(sensor.read_temperature()))

    pressure = float('{0:.1f}'.format(sensor.read_pressure() / 100))

    humidity = float('{0:.1f}'.format(sensor.read_humidity()))

    try:
        with open('BME280.csv', 'a') as f:
            thewriter = csv.writer(f)
            thewriter.writerow(["Time =", float(dateTime()), "Temperature =", temperature, "Pressure =", pressure, "Humidity =", humidity])
    except:
        pass
    
    return [temperature,pressure,humidity]

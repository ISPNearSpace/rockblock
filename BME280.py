import os
import time
import datetime
import glob
from time import strftime
from Adafruit_BME280 import *
import csv

sensor = BME280(t_mode=BME280_OSAMPLE_8, p_mode=BME280_OSAMPLE_8, h_mode=BME280_OSAMPLE_8)

def dateTime():  # get UNIX time
    secs = float(time.time())
    secs = secs * 1000
    return secs


def tempRead():  # read temperature, return float with 3 decimal points
    degrees = float('{0:.3f}'.format(sensor.read_temperature()))
    return degrees


def pressRead():  # read pressure, return float with 3 decimal points
    pascals = float('{0:.3f}'.format(sensor.read_pressure() / 100))
    return pascals


def humidityRead():  # read humidity, return float with 3 decimal points
    humidity = float('{0:.3f}'.format(sensor.read_humidity()))
    return humidity


secs = float(dateTime())
temperature = float(tempRead())
pressure = float(pressRead())
humidity = float(humidityRead())

with open('BME280.csv', 'a') as f:
    thewriter = csv.writer(f)
    thewriter.writerow(["Secs =", secs, "Temperature =", temperature, "Pressure =", pressure, "Humidity =", humidity])
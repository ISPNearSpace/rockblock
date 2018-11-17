import os
import time
import datetime
import glob
from time import strftime
from Adafruit_CCS811 import Adafruit_CCS811
import csv

ccs = Adafruit_CCS811()

def save_data(): # main functions to be called from rockblock
    def dateTime():  # get UNIX time
        secs = float(time.time())
        secs = secs * 1000
        return secs

    def co2Read():  # read co2, return float with 3 decimal points
        co2 = float('{0:.3f}'.format(ccs.geteCO2()))
        return co2

    def tvocRead():  # read tvoc, return float with 3 decimal points
        tvoc = float('{0:.3f}'.format(ccs.getTVOC()))
        return tvoc

    secs = float(dateTime())
    co2 = float(co2Read())
    tvoc = float(tvocRead())

    with open('CCS811.csv', 'a') as f:
        thewriter = csv.writer(f)
        thewriter.writerow(["Secs =", secs, "CO2 (ppm) =", co2, "TVOC =", tvoc])

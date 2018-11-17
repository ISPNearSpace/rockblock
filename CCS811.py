import os
import time
import datetime
import glob
from time import strftime
from Adafruit_CCS811 import Adafruit_CCS811
import csv

ccs = Adafruit_CCS811()

def save_data(): # main functions to be called from rockblock
    secs = float(time.time()) * 1000

    co2 = float('{0:.3f}'.format(ccs.geteCO2()))

    tvoc = float('{0:.3f}'.format(ccs.getTVOC()))

    with open('CCS811.csv', 'a') as f:
        thewriter = csv.writer(f)
        thewriter.writerow(["Secs =", secs, "CO2 (ppm) =", co2, "TVOC =", tvoc])

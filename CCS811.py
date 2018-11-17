import os
import time
import datetime
import glob
from time import strftime
from Adafruit_CCS811 import Adafruit_CCS811
import csv

ccs = Adafruit_CCS811()

def save_data(): # main functions to be called from rockblock
	if ccs.available():
	    if not ccs.readData():
		    with open('CCS811.csv', 'a') as f:
			thewriter = csv.writer(f)
			thewriter.writerow(["CO2: ", ccs.geteCO2(), "ppm, TVOC: ", ccs.getTVOC()])

save_data()

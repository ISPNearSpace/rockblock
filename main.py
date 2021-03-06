import protocol
from time import sleep
import sys

#sys.path.append('/nsp/Adafruit_GPIO/Adafruit_Python_BNO055')
sys.path.append('/home/pi/nsp/Adafruit_GPIO/Adafruit_Python_BME280')
sys.path.append('/home/pi/nsp/Adafruit_Python_GPIO/Adafruit_CCS811_python')
#import BNO055
import BME280
import CCS811


SLEEP_TIME = 30
rb = protocol.RockBlock("/dev/serial0")


# Structure: temperature,pressure,altitude,accelerometer,gyroscope
def make_string(params):
    s = ",".join(params)
    return s


def get_data():
    try:
        CCS811.save_data()
    except:
        pass

    # Data that will be sent
    p1 = []
    p2 = []
    try:
        p1 = BNO055.get_data()
    except:
        pass

    try:
        p2 = BME280.get_data()
    except:
        pass

    return p1 + p2


while True:
    data = get_data()
    try:
        s = make_string(data)
        rb.send_message(s)
    except:
        pass

    sleep(SLEEP_TIME)

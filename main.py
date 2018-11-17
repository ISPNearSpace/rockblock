import protocol
from time import sleep
import BNO055
import BME280


SLEEP_TIME = 5
rb = protocol.RockBlock("/dev/serial0")


# Structure: temperature,pressure,altitude,accelerometer,gyroscope
def make_string(params):
    s = ",".join(params)
    return s


def get_data():
    p1 = BNO055.get_data()
    p2 = BME280.get_data()

    return p1 + p2


while True:
    data = get_data()
    s = make_string(data)
    rb.send_message(s)

    sleep(SLEEP_TIME)

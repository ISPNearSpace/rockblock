import protocol
from time import sleep

SLEEP_TIME = 30
rb = protocol.RockBlock("/dev/serial0")


def make_string():
    pass


def get_data():
    return "probandooo"


while True:
    data = get_data()
    rb.send_message(data)

    sleep(SLEEP_TIME)
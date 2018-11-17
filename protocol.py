import glob
import signal
import sys
import time
from serial import Serial


class RockBlock (object):
    def __init__(self, portId):
        self.portId = portId
        self.s = Serial(self.portId, 19200)

        # self.s.write("ATE1\r")  # Enable echo
        self.s.write("AT&K0\r")  # Disable Flow Control
        # self.s.write("AT+SBDMTA=0\r")  # _disableRingAlerts

    def send_message(self, msg):
        self.s.write("AT\r")
        if self.s.readline().strip() == "AT":
            print self.s.readline().strip()


        command = "AT+SBDWT=" + str(msg)

        self.s.write(command + "\r")

        self.s.write("AT+SBDIX\r")

        return True
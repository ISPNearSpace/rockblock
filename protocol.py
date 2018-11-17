import glob
import signal
import sys
import time
from serial import Serial


class RockBlock (object):
    def __init__(self, portId):
        self.portId = portId
        self.s = Serial(self.portId, 19200)

    def send_message(self, msg):
        self.s.write("AT&K0\r")
        
        self.s.write("AT+SBDWT={}\r".format(msg))

        self.s.write("AT+SBDIX\r")

        return True
    
    def check_connection(self):
        command = "AT+CSQ"
        
        self.s.write(command + "\r")
             
        if( self.s.readline().strip() == command):
        
            response = self.s.readline().strip()
                  
            if( response.find("+CSQ") >= 0 ):
                            
                self.s.readline().strip()    #OK
                self.s.readline().strip()    #BLANK
                                        
                if( len(response) == 6):
                
                    return int( response[5] )
            
        return -1 

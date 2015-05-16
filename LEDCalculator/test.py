from LED import *

class Tester:
    _leds = []
    
    def __init__(self,leds):
        self._leds = leds
        
    def operate(self):
        for led in self._leds:
            if isinstance(led, LED):
                print(led.getState())
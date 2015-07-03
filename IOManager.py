import RPi.GPIO as GPIO
from LED import LED

class IOManager:
    """
    Manages in synchronizes software to hardware
    """
    
    _leds = []
    
    def __init__(self,leds):
        """
        Initializes the hardware board in BOARD-Layout without GPIO warnings
        """
        self._leds = leds
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        
        for led in self._leds:
            GPIO.setup(led.getPin(),GPIO.OUT)
            
    def synchronizeOutput(self):
        """
        Synchronizes the hardware LEDs to the software LED objects
        """
        if isinstance(self._leds[0], LED):
            
            for led in self._leds:
                GPIO.output(led.getPin(),led.getState())
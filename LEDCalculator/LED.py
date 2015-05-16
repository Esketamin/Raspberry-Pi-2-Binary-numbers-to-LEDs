class LED:
    _pin = 0
    _state = 0
    
    def __init__(self,pin,state):
        """
        Constructor
        Initializes the LED Object with the GPIO pin the LED is connected to and the initial state
        @param pin: the GPIO pin, the LED is connected to
        @param state: the initial state of the LED: 1 is on and 0 is off
        """
        self._pin = int(pin)
        self._state = int(state)
        
    
    def switchState(self):
        """ 
        LED-Switcher
        Switches the state of the LED from on to off or vice versa. On is represented by 1 or True,
        off is represented by 0 or False
        """
        if (self._state == 1):
            self._state = 0
        else:
            self._state = 1
           
    def getState(self):
        """
        Returns the current state of the LED
        @return: 0 if LED is off, 1 if LED is on
        """
        return self._state
    
    def getPin(self):
        """
        Returns the GPIO pin of the RPi, the LED is connected to
        @requires: RPi.GPIO.setup(BOARD)
        @return: integer number of the bin
        """
        return self._pin
    
    def setState(self,state):
        """
        Sets the state of the LED
        @requires: state == 1 or state == 0
        """
        self._state = state

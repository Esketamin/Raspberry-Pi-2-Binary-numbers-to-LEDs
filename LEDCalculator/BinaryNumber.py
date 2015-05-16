from LED import *

class BinaryNumber:
    
    _number = 0b0
    
    def __init__(self,number):
        if isinstance(number, int):
            self._number = number
        else:
            print("use integer numbers")
            self._number = int(number)
        
    def increment(self,leds):
        """
        Increments the number the object holds. It does also write the new binary representation to the array of 
        leds
        @requires: leds != null
        @requires: leds.__len__ != 0
        @param leds: Array of LED Objects that is to be switched 
        """
        self._number += 1
        length = len(leds)
        index = 0
        while (index in range (0,length)):
            if leds[index].getState() != 0:
                leds[index].switchState()
            else:
                leds[index].switchState()
                break
            index += 1
    
    def decrement(self,leds):
        """
        Decrements the number the object holds. It does also write the new binary representation to the array of 
        leds
        @requires: leds != null
        @requires: leds.__len__ != 0
        @param leds: Array of LED Objects that is to be switched 
        """
        self._number -= 1
        length = len(leds)
        index = 0
        while (index in range (0,length)):
            if leds[index].getState() != 1:
                leds[index].switchState()
            else:
                leds[index].switchState()
                break
            index += 1
            
    def getNumber(self):
        """
        @return: the integer number the object holds
        """
        return self._number
    
    def getBinaryStringRepresentation(self):
        """
        @return: String containing the binary representation of the number beginning with 0b
        """
        return bin(self._number)
    
    def trivialNumberSet(self,number,leds):
        self._number = 0
        for led in leds:
            led.setState(0)
        for i in range (0,number):
            self.increment(leds)
       
                    
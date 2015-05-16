from time import sleep
from LED import *
from test import *
from BinaryNumber import BinaryNumber
  
led1 = LED(12,1)
led2 = LED(26,1)
led3 = LED(27,0)
led4 = LED(28,0)




leds = [led1, led2, led3, led4]

binGen = BinaryNumber(10)
print(binGen.getBinaryStringRepresentation())

binGen.trivialNumberSet(10, leds)
binGen.decrement(leds)
print(binGen.getBinaryStringRepresentation())

for led in leds:
    print(led.getState())

sleep(1)
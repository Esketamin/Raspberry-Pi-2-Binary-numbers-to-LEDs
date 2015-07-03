from time import sleep
from LED import LED
from BinaryNumber import BinaryNumber
  
led1 = LED(12,1)
led2 = LED(26,1)
led3 = LED(27,0)
led4 = LED(28,0)

leds = [led1, led2, led3, led4]

binary = BinaryNumber(4,10)
print(binary._bits)
print(binary.getBinaryStringRepresentation())
for i in range (0,binary._bits):
    print(binary._numberArray[i])

sleep(1)
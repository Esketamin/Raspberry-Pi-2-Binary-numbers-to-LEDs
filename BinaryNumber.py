class BinaryNumber:
    
    _number = 0b0
    _bits = 0
    _numberArray = []
    
    def __init__(self,bits,number):
        """
        Initializes the object.
        @param bits: the number of bits the number should hold. Given as an integer.
        @param number: the number, the object should hold given as an integer.
        """
        if isinstance(number, int):
            self._number = number
        else:
            print("use integer numbers")
            self._number = int(number)
        if isinstance(bits, int):
            self._bits = bits
        else:
            self._bits = int(bits)
        for i in range (0, self._bits):
            self._numberArray.append(0)
        self.trivialArraySet(number)
            
    def incrementArray(self):
        """
        Incrments the number, the object holds and changes the bitarray as well.
        """
        self._number += 1
        index = 0
        while index in range (0,self._bits):
            if self._numberArray[index] == 1:
                self._numberArray[index] = 0
            else:
                self._numberArray[index] = 1
                break
            index += 1
            
    def decrementArray(self):
        """
        Decrements the number, the object holds and changes the bitarray as well.
        """
        self._number -= 1
        index = 0
        while index in range (0,self._bits):
            if self._numberArray[index] == 0:
                self._numberArray[index] = 1
            else:
                self._numberArray[index] = 0
                break
            index += 1
            
    def getNumber(self):
        """
        @return: the integer number the object holds
        """
        return self._number
    
    def getBinaryStringRepresentation(self):
        """
        Returns a String containing the binary number.
        @return: String containing the binary representation of the number beginning with 0b
        """
        return bin(self._number)
       
    def trivialArraySet(self,number):
        """
        Sets the number the object holds as binary to the array held. The entries represent single bits.
        @param number: The integer number the array shall hold in the binary array
        """
        self._number = 0
        for state in self._numberArray:
            state = 0
        for i in range (0,number):
            self.incrementArray()
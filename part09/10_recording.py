# WRITE YOUR SOLUTION HERE:
class Recording:

    def __init__(self, length: int):
        self.length = length
        
    # A getter method
    @property
    def length(self):
        return self.__length
    
    # A setter method
    @length.setter
    def length(self, length):
        if length >= 0:
            self.__length = length
        else:
            raise ValueError

        

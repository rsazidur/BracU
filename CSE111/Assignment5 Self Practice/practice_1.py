class ABC:
    def __init__(self, x, y):
        self.__x = x
        self.y = y
        
    def details(self):
        print(f"X is: {self.__x}\nY is: {self.y}")
    
    def set_X(self, x):
        self.__x = x
        
    def get_X(self):
        return self.__x
    
    
a1 = ABC(5, 6)
a2 = ABC(15, 17)

a1.set_X(45)

print(a1.get_X())

a1.details()
class FinalT6A:
    temp = 3
 
    def __init__(self, x, p):
        self.sum, self.y = 0, 2
        FinalT6A.temp += 3
        self.y = self.temp - p
        self.sum = self.temp + x
        print(x, self.y, self.sum)
    
    def methodA(self):
        x, y = 0, 0
        y = y + self.y
        x = self.y + 2 + self.temp
        self.sum = x + y + self.methodB(self.temp, y)
        print(x, y, self.sum)
    
    def methodB(self, temp, n):
        x = 0
        FinalT6A.temp += 1
        self.y = self.y + (FinalT6A.temp)
        FinalT6A.temp -= 1
        x = x + 2 + n
        self.sum = self.sum + x + self.y
        print(x, self.y, self.sum)
        return self.sum

q1 = FinalT6A(2,1)
q1.methodA()
q1.methodA()





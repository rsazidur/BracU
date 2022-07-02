class Quiz3A:
    def __init__(self, k=None):
        self.temp, self.sum, self.y = 4, 0, 0
        if k != None:
            self.temp += 1
            self.temp = self.temp
            self.sum = self.temp + k
            self.y = self.sum - 1
        else:
            self.y = self.temp - 1
            self.sum = self.temp + 1
            self.temp += 2

    def methodB(self, m, n):

        x = 0
        self.temp += 1
        self.y = self.y + m + self.temp
        x = x + 2 + n
        self.sum = self.sum + x + self.y
        print(x, self.y, self.sum)
        return self.sum

a1 = Quiz3A()
a1.methodB(1, 2)
a2 = Quiz3A(3)
a2.methodB(2, 4)
a1.methodB(2, 1)
a2.methodB(1, 3)

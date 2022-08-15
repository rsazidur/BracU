class msgClass:
    def __init__(self):
        self.content = 0
 
class Quiz3:
    x = 0
    def __init__(self, k = None):
        self.sum, self.y = 0, 0
        if k is None:
            self.sum = 5
            Quiz3.x = 2
            self.y = 2
        else:
            self.sum = self.sum + k
            self.y = 3
            Quiz3.x += 2    
    def methodA(self):
        x = 1
        y = 1
        msg = [None]
        myMsg = msgClass()
        myMsg.content = Quiz3.x
        msg[0] = myMsg
        msg[0].content = self.y + myMsg.content
        self.y = self.y + self.methodB(msg[0])
        y = self.methodB(msg[0]) + self.y
        x = y + self.methodB(msg, msg[0])
        self.sum = x + y + msg[0].content
        print(x, y, self.sum)
    def methodB(self, *args):
        if len(args) == 2:
            mg2, mg1 = args
            x = 2
            self.y = self.y + mg2[0].content
            mg2[0].content = self.y + mg1.content
            x = x + 2 + mg1.content
            self.sum = self.sum + x + self.y
            mg1.content = self.sum - mg2[0].content
            print(Quiz3.x, self.y, self.sum)
            return self.sum
        
        elif len(args) == 1:
            mg1, = args
            x = 1
            y = 2
            y = self.sum + mg1.content
            self.y = y + mg1.content
            x = Quiz3.x + 5 + mg1.content
            self.sum = self.sum + x + y
            Quiz3.x = mg1.content + x + 3
            print(x, y, self.sum)
            return y

a1 = Quiz3()
a2 = Quiz3(5)
msg = msgClass()
a1.methodA()
a2.methodB(msg)

class myList:
    def __init__(self, *args):
        self.newlist = [i for i in args]
        
    def sum(self):
        print(f"Sum: {sum(self.newlist)}")

    def merge(self, *args):
        self.newlist += [i for i in args]   

    def average(self):
        print(f"Average: {sum(self.newlist) / len(self.newlist)}")


l1 =  myList(2,3,4,5,6)
l1.sum()
l1.merge(4,5,9)
l1.sum()
l1.average()
print("-----------------------------")
l2 =  myList(2,4,5,7)
l2.average()
l2.merge(1,2,4,8)
l2.sum()


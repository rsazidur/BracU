class Passenger:
    count = 0
    
    def __init__(self, name):
        self.name = name
        Passenger.count += 1
        
    def printDetail(self):
        print("Name:", self.name, "\nBus Fare:", Passenger.set_bag_weight)
    
    @staticmethod
    def set_bag_weight(weight):
        if weight <= 20:
            print(450)
        
        elif weight <= 50:
            print(450 + 50)
        
        elif weight > 50:
            print(450 + 100)    


print("Total Passenger:", Passenger.count)
p1 = Passenger("Jack")
p1.set_bag_weight(90)
p2 = Passenger("Carol")
p2.set_bag_weight(10)
p3 = Passenger("Mike")
p3.set_bag_weight(25)
print("=========================")
p1.printDetail()
print("=========================")
p2.printDetail()
print("=========================")
p3.printDetail()
print("=========================")
print("Total Passenger:", Passenger.count)
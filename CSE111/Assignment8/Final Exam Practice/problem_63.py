class Passenger:
    count = 0
    def __init__(self, name):
        self.name = name
        Passenger.count += 1
        
    def set_bag_weight(self, weight):
        self.weight = weight

        if weight < 20:
            self.weight = 450
        elif 21 < weight <= 50:
            self.weight = 500
        else:
            self.weight = 550

    def printDetail(self):
        print(f"Name: {self.name}\nBus Fare: {self.weight} Taka")
        

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
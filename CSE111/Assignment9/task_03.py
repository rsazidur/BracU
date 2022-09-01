class Bird:
    def __init__(self, name,flying=False):
        self.name = name
        self.flying = flying
        self.type = "Flightless Birds"

    def fly(self):
        if self.flying == True:
            print(f"{self.name} can fly")
        else:
            print(f"{self.name} can not fly")

    def setType(self, type):
        self.type = type

    def printDetail(self):
        print(f"Name: {self.name}\nType: {self.type}")

ostrich = Bird('Ostrich')
duck = Bird("Duck", True)
owl = Bird('Owl', True)
print("###########################")
ostrich.fly()
duck.fly()
owl.fly()
duck.setType('Water Birds')
owl.setType('Birds of Prey')
print("=========================")
ostrich.printDetail()
print("=========================")
duck.printDetail()
print("=========================")
owl.printDetail()


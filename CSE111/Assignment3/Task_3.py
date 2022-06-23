class Patient:
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    def printDetails(self):
        print(f"Name:", self.name)
        print(f"Age:", self.age)
        print(f"Weight:{self.weight} kg")
        print(f"Height:{self.height} cm")
        bmi = self.weight / (self.height / 100 * self.height / 100)
        print(f"Bmi:", bmi)


p1 = Patient("A", 55, 63.0, 158.0)
p1.printDetails()
print("====================")
p2 = Patient("B", 53, 61.0, 149.0)
p2.printDetails()
class Laptop:
    laptopCount = 0
    
    def __init__(self, name, count):
        self.name = name
        self.count = count
        Laptop.laptopCount += self.count
  
    @staticmethod
    def advantage():
        print("Laptops are portable")
        
    @staticmethod
    def resetCount():
        Laptop.laptopCount = 0
        return f"Total number of Laptops {Laptop.laptopCount}"
    



lenovo = Laptop("Lenovo", 5);
dell = Laptop("Dell", 7);
print(lenovo.name, lenovo.count)
print(dell.name, dell.count)
print("Total number of Laptops", Laptop.laptopCount)
Laptop.advantage()
Laptop.resetCount()
print("Total number of Laptops", Laptop.laptopCount)
class Assassin:
    number = 0
    def __init__(self, name, rate):
        self.name = name
        self.rate = rate
        Assassin.number += 1
        
    def printDetails(self):
        print(f"Name: {self.name} \nSuccess rate: {self.rate}%"
              f"\nTotal number of Assassin: {Assassin.number}")
              
    @classmethod
    def failureRate(cls, name, f_rate):
        success = 100 - f_rate
        return cls(name, success)
    
    @classmethod
    def failurePercentage(cls, name, f_Percentage):
        success = 100 - int(f_Percentage[:-1])
        return cls(name, success)

john_wick = Assassin('John Wick', 100)
john_wick.printDetails()
print('================================')
nagisa = Assassin.failureRate("Nagisa", 20)
nagisa.printDetails()
print('================================')
akabane = Assassin.failurePercentage("Akabane", "10%")
akabane.printDetails()
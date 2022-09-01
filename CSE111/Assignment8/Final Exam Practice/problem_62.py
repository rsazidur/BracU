from sre_constants import SUCCESS


class Assassin:
    No_of_assassin = 0
    
    def __init__(self, name, success):
        self.name = name
        self.success = success
        Assassin.No_of_assassin += 1
    
    def printDetails(self):
        print(f"Name: {self.name}\nSuccess rate: {self.success}%\nTotal number of Assassin: {Assassin.No_of_assassin}")

    @classmethod
    def failureRate(cls, name, f_rate):
        sucess_rate = 100 - f_rate
        return cls(name, sucess_rate)

    @classmethod
    def failurePercentage(cls, name, p_rate):
        success_rate = 100 - int(p_rate[:-1])
        return cls(name, success_rate)


john_wick = Assassin('John Wick', 100)
john_wick.printDetails()
print('================================')
nagisa = Assassin.failureRate("Nagisa", 20)
nagisa.printDetails()
print('================================')
akabane = Assassin.failurePercentage("Akabane", "10%")
akabane.printDetails()
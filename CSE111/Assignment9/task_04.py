from functools import total_ordering


class Account:
    count = 0

    def __init__(self, name, age, occupation, totalAmount):
        self.name = name
        self.age = age
        self.occupation = occupation
        self.totalAmount = totalAmount
        Account.count += 1

    def addMoney(self, money):
        self.totalAmount += money
    
    def withdrawMoney(self, money):
        if self.totalAmount >= money:
            self.totalAmount -= money
        pass

    def printDetails(self):
        print(f"Name: {self.name}\nAge: {self.age}\nOccupation: {self.occupation}\nTotal Amount: {self.totalAmount}")

print('No of account holders:', Account.count)
print("=========================")
p1 = Account("Abdul", 45, "Service Holder", 500000)
p1.addMoney(300000)
p1.printDetails()
print("=========================")
p2 = Account("Rahim", 55, "Businessman", 700000)
p2.withdrawMoney(700000)
p2.printDetails()
print("=========================")
p3 = Account("Ashraf", 62, "Govt. Officer", 200000)
p3.withdrawMoney(250000)
p3.printDetails()
print("=========================") 
print('No of account holders:', Account.count)

class Account:
    def __init__(self, name=None, balance=None):
        self.name = name
        self.balance = balance

        print("Default Account")
        print("0.0")

    def withdraw(self):

    def details(self):
        pass

a1 = Account()
print(a1.details())
print("------------------------")
a1.name = "Oliver"
a1.balance = 10000.0
print(a1.details())
print("------------------------")
a2 = Account("Liam")
print(a2.details())
print("------------------------")
a3 = Account("Noah", 400)
print(a3.details())
print("------------------------")
a3.withdraw(6930)
print("------------------------")
a2.withdraw(600)
print("------------------------")
a1.withdraw(6929)
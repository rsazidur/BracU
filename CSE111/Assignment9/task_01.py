class PlayerEarning:
    def __init__(self, name):
        self.name = name
    
    def calculateTotal(self, salary, goal=0):
        self.salary = salary
        self.goal = goal
        self.bonus = 0
        
        if self.goal > 30:
            self.bonus = int((5/100) * self.salary + 10000)
        else:
            self.bonus = int((5/100) * self.salary)
        
    def printDetails(self):
        print(f"Player Name: {self.name}\nPlayer Season Earning without bonus: {self.salary}"
        f"\nBonus: {self.bonus}\nPlayer Season Earning After Bonus: {self.salary + self.bonus}")



print("**********************")
player1 = PlayerEarning('Buffon')
player1.calculateTotal(250000)
player1.printDetails()

print("\n**********************")
player2 = PlayerEarning('Dybala')
player2.calculateTotal(250000, 31)
player2.printDetails()

print("\n**********************")
player3 = PlayerEarning('Cuadrado')
player3.calculateTotal(250000, 20)
player3.printDetails()

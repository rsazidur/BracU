class Calculator:
    def __init__(self):
        print("Calculator is Ready!")
        self.first_value = 0
        self.second_value = 0
        self.operator = None

    def calculate(self):
        val = self.first_value, self.operator
    def showCalculation(self):
        if self.operator == "+":
            Calculator.add(self)
        elif self.operator == "-":
            Calculator.subtract(self)
        elif self.operator == "*":
            Calculator.multiply(self)
        elif self.operator == "/":
            Calculator.divide(self)

    def add(self):
        print(f"Result : {self.first_value + self.second_value}")

    def subtract(self):
        print(f"Result : {self.first_value - self.second_value}")

    def multiply(self):
        print(f"Result : {self.first_value * self.second_value}")

    def divide(self):
        print(f"Result : {self.first_value / self.second_value}")

if __name__ == "__main__":

    c1 = Calculator()
    print("==================")
    val = c1.calculate(10, 20, '+')
    print("Returned value:", val)
    c1.showCalculation()
    print("==================")
    val = c1.calculate(val, 10, '-')
    print("Returned value:", val)
    c1.showCalculation()
    print("==================")
    val = c1.calculate(val, 5, '*')
    print("Returned value:", val)
    c1.showCalculation()
    print("==================")
    val = c1.calculate(val, 16, '/')
    print("Returned value:", val)
    c1.showCalculation()
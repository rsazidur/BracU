class Calculator:
    def __init__(self):
        self.first_value = None
        self.second_value = None
        self.operator = None
        print("Calculator is Ready!")

    def calculate(self, first_value, second_value, operator):
        self.first_value = first_value
        self.second_value = second_value
        self.operator = operator

        if operator == "+":
            val = first_value + second_value
            return val

        elif operator == "-":
            val = first_value - second_value
            return val

        elif operator == "*":
            val = first_value * second_value
            return val

        elif operator == "/":
            val = first_value / second_value
            return val

    def showCalculation(self):

        if self.operator == "+":
            print(f"{self.first_value} + {self.second_value} = {val}")

        elif self.operator == "-":
            print(f"{self.first_value} - {self.second_value} = {val}")

        elif self.operator == "*":
            print(f"{self.first_value} * {self.second_value} = {val}")

        elif self.operator == "/":
            print(f"{self.first_value} / {self.second_value} = {val}")


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
class Calculator:
    def __init__(self, first_value, second_value, operator):
        self.first_value = first_value
        self.second_value = second_value
        self.operator = operator

    def calculate(self):
        val = self.first_value, self.operator
    def showCalculation(self):
        pass

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
class Employee:
    def __init__(self, name, workingPeriod):
        self.name = name
        self.workingPeriod = workingPeriod
        
    @classmethod
    def employeeByJoiningYear(cls, name, year):
        workingPeriod = 2022 - year
        return Employee(name, workingPeriod)
    
    @staticmethod
    def experienceCheck(workingPeriod, gender):
        if workingPeriod < 3 and gender == "male":
            return("He is not experienced")
        elif workingPeriod >= 3  and gender == "male":
            return("He is experienced")
        
        elif workingPeriod < 3 and gender == "female":
            return("She is not experienced")
        elif workingPeriod >= 3  and gender == "female":
            return("She is experienced")



employee1 = Employee('Dororo', 3)
employee2 = Employee.employeeByJoiningYear('Harry', 2016)
print(employee1.workingPeriod)
print(employee2.workingPeriod)
print(employee1.name)
print(employee2.name)
print(Employee.experienceCheck(2, "male"))
print(Employee.experienceCheck(3, "female"))
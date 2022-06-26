class Student:
    def __init__(self, name, id, department, credit):
        self.name = name
        self.id = id
        self.department = department
        self.credit = credit
        self.cgpa = 0

    def calculate_CGPA(self):
        summation = 0
        for item in self.credit:
            summation += item
        self.cgpa = summation / len(self.credit)
git
    def print_details(self):
        if self.cgpa > 3.80:
            print(f"Name: {self.name}, ID: {self.id}")
            print(f"Department: {self.department}")
            print(f"CGPA: {self.cgpa}")
            print("Your academic standing is 'Highest Distinction'")

        elif self.cgpa > 3.65:
            print(f"Name: {self.name}, ID: {self.id}")
            print(f"Department: {self.department}")
            print(f"CGPA: {self.cgpa}")
            print("Your academic standing is 'High Distinction'")

        elif self.cgpa > 3.50:
            print(f"Name: {self.name}, ID: {self.id}")
            print(f"Department: {self.department}")
            print(f"CGPA: {self.cgpa}")
            print("Your academic standing is 'Distinction'")

        elif self.cgpa > 2.00:
            print(f"Name: {self.name}, ID: {self.id}")
            print(f"Department: {self.department}")
            print(f"CGPA: {self.cgpa}")
            print("Your academic standing is 'Satisfactory'")

        elif self.cgpa < 2.00:
            print(f"Name: {self.name}, ID: {self.id}")
            print(f"Department: {self.department}")
            print(f"CGPA: {self.cgpa}")
            print("Sorry, you cannot graduate")


s1 = Student('Dora', '15995599', 'CSE', [4, 3.7, 3.7, 4])
s1.calculate_CGPA()
print("==========================")
s1.print_details()
print("==========================")
s2 = Student('Pingu', '12312322', 'EEE', [1.7, 1.3, 1.3, 1.3, 1])
s2.calculate_CGPA()
print("==========================")
s2.print_details()
print("==========================")
s3 = Student('Bob', '13311331', 'CSE', [2, 3, 3, 3.7, 2.7, 2.7])
s3.calculate_CGPA()
print("==========================")
s3.print_details()

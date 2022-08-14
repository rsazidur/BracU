class Student:
    t_student = 0
    b_student = 0
    o_student = 0

    def __init__(self, name, dept, uni="Brac University"):
        self.name = name
        self.dept = dept
        self.uni = uni
        Student.t_student += 1
        if self.uni != "Brac University":
            Student.o_student += 1
        else:
            Student.b_student += 1

    @classmethod
    def createStudent(cls, name, dept, uni="Brac University"):
        
        return Student(name, dept, uni)
        

    @staticmethod
    def printDetails():
        print("Total Student(s):",Student.t_student,
        "\nBRAC University Student(s):", Student.b_student,
        "\nOther Institution Student(s):", Student.o_student)

    def individualDetail(self):
        print(f"Name: {self.name} \nDepartment: {self.dept} \nInstitution:{self.uni}")


Student.printDetails()
print('#########################')
mikasa = Student('Mikasa Ackerman', "CSE")
mikasa.individualDetail()
print('------------------------------------------')
Student.printDetails()
print('========================')
harry = Student.createStudent('Harry Potter', "Defence Against Dark Arts", "Hogwarts School")
harry.individualDetail()
print('-------------------------------------------')
Student.printDetails()
print('=========================')
levi = Student.createStudent("Levi Ackerman", "CSE")
levi.individualDetail()
print('--------------------------------------------')
Student.printDetails()
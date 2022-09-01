import getpass


class Student:
    def __init__(self,name,ID):
        self.name = name
        self.ID = ID
    def Details(self):
        return "Name: "+self.name+"\n"+"ID: "+self.ID+"\n"
#Write your code here


class CSEStudent(Student):
    def __init__(self, name, ID, semester):
        super().__init__(name, ID)
        self.semester = semester
        self.marks = {}
        self.gpa = 0

    def Details(self):
        return super().Details() + "Current semester: "+ self.semester

    def addCourseWithMarks(self, *info):
        total = 0.0
        for i in range(0, len(info), 2):
            gpa = 0
            mark = info[i + 1]

            if mark >= 85:
                gpa = 4.0
            elif 80 <= mark <= 84:
                gpa = 3.3
            elif 70 <= mark <= 79:
                gpa = 3.0
            elif 65 <= mark <= 69:
                gpa = 2.3
            elif 57 <= mark <= 64:
                gpa = 2.0
            elif 55 <= mark <= 56:
                gpa = 1.3
            elif 50 <= mark <= 54:
                gpa = 1.0

            self.marks[info[i]] = gpa
            total += gpa

        self.gpa = total / len(self.marks)

    def showGPA(self):
        print(f"{self.name} has taken {len(self.marks)} courses.")
        for i, j in self.marks.items():
            print(i + ": ", j)
        print(f"GPA of {self.name} is {round(self.gpa, 2)}")



Bob = CSEStudent("Bob","20301018","Fall 2020")
Carol = CSEStudent("Carol","16301814","Fall 2020")
Anny = CSEStudent("Anny","18201234","Fall 2020")
print("#########################")
print(Bob.Details())
print("#########################")
print(Carol.Details())
print("#########################")
print(Anny.Details())
print("#########################")
Bob.addCourseWithMarks("CSE111",83.5,"CSE230",73.0,"CSE260",92.5)
Carol.addCourseWithMarks("CSE470",62.5,"CSE422",69.0,"CSE460",76.5,"CSE461",87.0)
Anny.addCourseWithMarks("CSE340",45.5,"CSE321",95.0,"CSE370",91.0)
print("----------------------------")
Bob.showGPA()
print("----------------------------")
Carol.showGPA()
print("----------------------------")
Anny.showGPA()

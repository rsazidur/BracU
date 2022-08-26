class Exam: 
    def __init__(self,marks): 
        self.marks = marks 
        self.time = 60 
         
    def examSyllabus(self): 
        return "Maths , English" 
    def examParts(self): 
        return "Part 1 - Maths\nPart 2 - English\n" 


class ScienceExam(Exam):
    def __init__(self, marks, time, *subject):
        super().__init__(marks)
        self.time = time
        self.sub_det = []
        self.no = 2
        for i in subject:
            self.no += 1
            self.sub_det.append(i)

    def examSyllabus(self):
        sublist = super().examSyllabus()
        for item in self.sub_det:
            sublist +=", " + item
        return sublist

    def examParts(self):
        part = super().examParts()
        counter = 3

        for item in self.sub_det:
            part += f"part {str(counter)} - {item}\n"
            counter += 1
        return part

    def __str__(self):
        return f"Marks: {str(self.marks)} Time: {str(self.time)} Number of Parts: {str(self.no)}"
     
engineering = ScienceExam(100, 90, "Physics", "HigherMaths")
print(engineering)
print("----------------------------------")
print(engineering.examSyllabus())
print(engineering.examParts())
print("==================================")
architecture = ScienceExam(100, 120, "Physics", "HigherMaths", "Drawing")
print(architecture)
print("----------------------------------")
print(architecture.examSyllabus())
print(architecture.examParts())
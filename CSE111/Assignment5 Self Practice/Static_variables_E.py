class Student:
    count = 0
    
    def __init__(self, name, Id):
        self.name = name
        self.id = Id
        Student.count += 1      # It's work on constructor 
        
    def details(self):
        print(f"Name: {self.name} Id: {self.id}")
        

s1 = Student("Bob", 11)
s2 = Student("Carol", 22)
s3 = Student("Mike", 33)

s1.details()
s2.details()
s3.details()

print(f"Student count: {Student.count}")
class Student:
    uni_name = "BracU"
    
    def __init__(self, name, Id):
        self.name = name
        self.id = Id
        
    def details(self):
        print("Name: " , self.name, "\nId: " , self.id,
              "\nUniversity name: ", Student.uni_name)
    
    @classmethod
    def up_uni_name(cls, u_name):
        cls.uni_name = u_name
    
s1 = Student("Bob", 11)
s2 = Student("Carol", 22)

s1.details()
s2.details()

Student.up_uni_name("Brac University")

s1.details()
s2.details()
class Student:
    uni_name = "BracU"
    
    def __init__(self, name, Id):
        self.name = name
        self.id = Id
        
    def details(self):
        print("Name:", self.name, "Id: ", self.id,
              "\nUniversity:", Student.uni_name)
    
    @classmethod
    def up_Uni_Name(cls, u_name):
        cls.uni_name = u_name
    
    @classmethod
    def change_String(cls, string):
        name, Id = string.split("-")
        obj = Student(name, Id)
        return obj
    
s1 = Student("Bob", 11)
s2 = Student.change_String("Carol-22")

s1.details()
s2.details()
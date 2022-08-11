class Student:
    uni_name = "BracU"              # class / static variable
    
    def __init__(self, name, Id):
        self.name = name
        self.id = Id
        
    def details(self):
        print("Name: " , self.name, "\nId: " , self.id,
              "\nUniversity name: ", Student.uni_name)
    
    @classmethod
    def up_uni_name(cls, u_name):   # We are changeing the name
        cls.uni_name = u_name
    
s1 = Student("Bob", 11)
s2 = Student("Carol", 22)

s1.details()                # Before changing the name
s2.details()

Student.up_uni_name("Brac University")  # we call the method and changed the name

s1.details()                # After changing the name
s2.details()
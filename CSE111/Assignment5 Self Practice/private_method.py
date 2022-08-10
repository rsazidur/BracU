class Student:
    def __init__(self, name, Id):
        self.name = name   # instance variable
        self.__id = Id     # private variable
        
        
    def details(self):      # instance variable
        print(f"Name: {self.name} \nID: {self.__id}")
        self.__method()
    
    def __method(self):     # private variable
        print("Private method executed.")
        
        
s1 = Student("Bob", 12)
s2 = Student("Carol", 24)

#s1.__method()               # 'Student' object has no attribute '__method'

s1.details()
s2.details()
    
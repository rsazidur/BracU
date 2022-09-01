from unicodedata import name


class Smartphone:
    def __init__(self, string=""):
        self.string = string
        self.display = ""
        self.display_name = ""
        self.ram_size = ""
        self.ram_type = ""

    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name

    def addFeature(self, display, size):
        if self.string == "":
            print("Feature can not be added without phone name")

        if display == "Display":
            self.display = display
            self.display_name = self.display_name + ", " + size
        elif display == "Ram":
            self.ram_size = display
            self.ram_type = self.ram_type + ", " + size

    def printDetail(self):
        print(f'Phone Name: {self.name}\nDisplay: {self.display_name}\nRam: {self.ram_size}: {self.ram_type}')
        

        


s1 = Smartphone()
print("=================================")
s1.addFeature("Display", "6.1 inch")
print("=================================")
s1.setName("Samsung Note 20")
s1.addFeature("Display", "6.1 inch")
s1.printDetail()
print("=================================")
s2 = Smartphone("Iphone 12 Pro")
s2.addFeature("Display", "6.2 inch")
s2.addFeature("Ram", "6 GB")
print("=================================")
s2.printDetail()
s2.addFeature("Display", "Amoled panel")
s2.addFeature("Ram", "DDR5")
print("=================================")
s2.printDetail()
print("=================================")

from math import radians


class Cylinder:
    radius = 5
    height = 18

    def __init__(self, radius, height):
        print(f"Default radius={Cylinder.radius} and height={Cylinder.height}.")
        Cylinder.radius = radius
        Cylinder.height = height
        print(f"Updated: radius={Cylinder.radius} and height={Cylinder.height}.")

    
    @staticmethod
    def area(radius, height):
        print(f"Area: {2 * 3.1416 * (radius ** 2) + 2 * 3.1416 * radius * height}")

    @staticmethod
    def volume(radius, height):
        print(f"Volume: {3.1416 * (radius ** 2) * height}")

    @classmethod
    def swap(cls, radius, height):
        return Cylinder(height, radius)

    @classmethod
    def changeFormat(cls, dash):
        radius, height = dash.split("-")
        return Cylinder (int(radius), int(height))

    

c1 = Cylinder(0,0)
Cylinder.area(c1.radius,c1.height)
Cylinder.volume(c1.radius,c1.height)
print("===============================")
c2 = Cylinder.swap(8,3)
c2.area(c2.radius,c2.height)
c2.volume(c2.radius,c2.height)
print("===============================")
c3 = Cylinder.changeFormat("7-13")
c3.area(c3.radius,c3.height)
c3.volume(c3.radius,c3.height)
print("===============================")
Cylinder(0.3,5.56).area(Cylinder.radius,Cylinder.height)
print("===============================")
Cylinder(3,5).volume(Cylinder.radius,Cylinder.height)
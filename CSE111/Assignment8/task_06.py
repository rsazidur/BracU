class Shape3D:
    pi = 3.14159

    def __init__(self, name="Default", radius=0):
        self._area = 0
        self._name = name
        self._height = "No need"
        self._radius = radius

    def calc_surface_area(self):
        return 2 * Shape3D.pi * self._radius

    def __str__(self):
        return "Radius: " + str(self._radius)


class Sphere(Shape3D):
    def __init__(self, name, radius):
        super().__init__(name, radius)
        print(f"Shape name: {self._name}, Area Formula: 4 * pi * r * r")

    def calc_surface_area(self):
        self._Area = 4 * Shape3D.pi * self._radius * self._radius
        return self._Area

    def __str__(self):
        return f"Radius: {self._name}, Height: {str(self._radius)} Area: {str(self._Area)}"


class Cylinder(Shape3D):
    def __init__(self, name='Cylinder', radius=0, height=0):
        super().__init__(name, radius)
        self._height = height
        print(f"Shape name: {self._name}, Area Formula: 2 * pi * r * (r + h)")
        
    def calc_surface_area(self):
        self._Area = 2 * Shape3D.pi * self._radius * (self._radius + self._height)
        return self._Area

    def __str__(self):
        return f"Radius: {str(self._radius)} Height: {str(self._height)}\nArea: {str(self._Area)}"

sph = Sphere("Sphere", 5)
print("----------------------------------")
sph.calc_surface_area()
print(sph)
print("==================================")
cyl = Cylinder("Cylinder", 5, 10)
print("----------------------------------")
cyl.calc_surface_area()
print(cyl)
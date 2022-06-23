class Shape:
    def __init__(self, name, angle1, angle2):
        self.name = name
        self.angle1 = angle1
        self.angle2 = angle2

    def area(self):

        if self.name == "Triangle" or self.name == "Rhombus":
            print(f"Area: {0.5 * self.angle1 * self.angle2}")

        elif self.name == "Square" or self.name == "Rectangle":
            print(f"Area: {self.angle1 * self.angle2}")

        else:
            print(f"Area: Shape unknown")


if __name__ == "__main__":
    triangle = Shape("Triangle", 10, 25)
    triangle.area()
    print("==========================")
    square = Shape("Square", 10, 10)
    square.area()
    print("==========================")
    rhombus = Shape("Rhombus", 18, 25)
    rhombus.area()
    print("==========================")
    rectangle = Shape("Rectangle", 15, 30)
    rectangle.area()
    print("==========================")
    trapezium = Shape("Trapezium", 15, 30)
    trapezium.area()

class Box:
    def __init__(self, list1):
        height, width, breadth = list1

        self.height = height
        self.width = width
        self.breadth = breadth

        print("Creating a Box!")
        print(f"Volume of the box is {height * width * breadth} cubic units.")


if __name__ == "__main__":
    print("Box 1")
    b1 = Box([10, 10, 10])
    print("=========================")
    print("Height:", b1.height)
    print("Width:", b1.width)
    print("Breadth:", b1.breadth)
    print("-------------------------")
    print("Box 2")
    b2 = Box((30, 10, 10))
    print("=========================")
    print("Height:", b2.height)
    print("Width:", b2.width)
    print("Breadth:", b2.breadth)
    b2.height = 300
    print("Updating Box 2!")
    print("Height:", b2.height)
    print("Width:", b2.width)
    print("Breadth:", b2.breadth)
    print("-------------------------")
    print("Box 3")
    b3 = b2
    print("Height:", b3.height)
    print("Width:", b3.width)
    print("Breadth:", b3.breadth)
class Color:
    def __init__(self, clr):
        self.clr = clr

    def __add__(self, other):
        colors = (self.clr, other.clr)
        if "red" in colors and "yellow" in colors:
            return Color("Orange")
        elif "yellow" in colors and "blue" in colors:
            return Color("Green")
        elif "blue" in colors and "red" in colors:
            return Color("Violet")


if __name__ == "__main__":
    C1 = Color(input("First Color: ").lower())
    C2 = Color(input("Second Color: ").lower())
    C3 = C1 + C2
    print("Color formed:", C3.clr)
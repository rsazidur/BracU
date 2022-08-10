class Dolls:

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.info = f"Doll: {self.name} \nPrice: {self.price}"

    def __gt__(self, other):
        if self.price > other.price:
            return True
        return False

    def detail(self):
        return self.info

    def __add__(self, other):
        x = Dolls(self.name + " " + other.name, self.price + other.price)
        x.info = x.info[:4] + "s" + x.info[4:]
        return x


if __name__ == "__main__":

    obj_1 = Dolls("Tweety", 2500)
    print(obj_1.detail())
    if obj_1 > obj_1:
        print("Congratulations! You get the Tweety as a gift!")
    else:
        print("Thank you!")
    print("=========================")
    obj_2 = Dolls("Daffy Duck", 1800)
    print(obj_2.detail())
    if obj_2 > obj_1:
        print("Congratulations! You get the Tweety as a gift!")
    else:
        print("Thank you!")
    print("=========================")
    obj_3 = Dolls("Bugs Bunny", 3000)
    print(obj_3.detail())
    if obj_3 > obj_1:
        print("Congratulations! You get the Tweety as a gift!")
    else:
        print("Thank you!")
    print("=========================")
    obj_4 = Dolls("Porky Pig", 1500)
    print(obj_4.detail())
    if obj_4 > obj_1:
        print("Congratulations! You get the Tweety as a gift!")
    else:
        print("Thank you!")
    print("=========================")
    obj_5 = obj_2 + obj_3
    print(obj_5.detail())
    if obj_5 > obj_1:
        print("Congratulations! You get the Tweety as a gift!")
    else:
        print("Thank you!")
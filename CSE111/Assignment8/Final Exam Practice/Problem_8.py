from typing import Coroutine


class Coordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return "The calculated coordinates are the same."
        else:
            return "The calculated coordinates are NOT the same."

    def __sub__(self, other):
        return Coordinates(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Coordinates(self.x * other.x, self.y * other.y)

    def detail(self):
        return self.x, self.y



p1 = Coordinates(int(input()),int(input()))
p2 = Coordinates(int(input()),int(input()))
p4 = p1 - p2
print(p4.detail())
p5 = p1 * p2
print(p5.detail())
point_check = (p4 == p5)
print(point_check)
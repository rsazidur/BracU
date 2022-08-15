class Puzzle:
    x = 0
    def methodA(self):
        Puzzle.x = 5 
        z = Puzzle.x + self.methodB(Puzzle.x)
        print(Puzzle.x, z)
        z = self.methodB(z + 2) + Puzzle.x
        print(Puzzle.x, z)
        self.methodB(Puzzle.x, z)
        print(Puzzle.x, z)
 
    def methodB(self, *args):
        if len(args) == 1:
            y = args[0]
            Puzzle.x = y + Puzzle.x
            print(Puzzle.x, y)
            return Puzzle.x + 3
        else:
            z, x = args
            z = z + 1
            x = x + 1
            print(z, x)

p = Puzzle()
p.methodA()
p.methodA()
p = Puzzle()
p.methodA()
p.methodB(7)
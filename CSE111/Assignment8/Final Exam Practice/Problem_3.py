class Team:
    def __init__(self, name=None):
        self.__name = name
        self.__player = []

    def setName(self, new):
        self.__name = new

    def addPlayer(self, player):
        self.__player.append(player)

    

class Player:
    def __init__(self, name):
        self.name = name
    
    def printDetail(self):
        print("=====================")
        print(f"Team:{self.__name}\nList of Player:")
        print([(i.name) for i in self.__player])
        print("=====================")

b = Team()
b.setName('Bangladesh')
mashrafi = Player("Mashrafi")
b.addPlayer(mashrafi)
tamim = Player("Tamim")
b.addPlayer(tamim)
b.printDetail()
a = Team("Australia")
ponting = Player("Ponting")
a.addPlayer(ponting)
lee = Player("Lee")
a.addPlayer(lee)
a.printDetail()
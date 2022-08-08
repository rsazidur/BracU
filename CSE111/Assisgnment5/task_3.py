class Team:
    def __init__(self, name=None):
        self.__name = name
        self.__players = []

    def setName(self, new):
        self.__name = new

    def addPlayer(self, new):
        self.__players.append(new)

    def printDetail(self):
        print("=====================")
        print(f"Team: {self.__name}")
        print("List of players")
        print([i.name for i in self.__players])
        
class Player:
    def __init__(self, name):
        self.name = name


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
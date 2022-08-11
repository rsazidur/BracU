class Player:
    
    team_run = 0                # static variables
    
    def __init__(self, run):
        self.run = run          # instance variables

    def hit_Four(self):
        self.run += 4
        Player.team_run += 4    # always call with class 
        
    def hit_Six(self):
        self.run += 6
        Player.team_run += 6
        
        
sakib = Player(0)
tamim = Player(0)

sakib.hit_Four()
sakib.hit_Six()

tamim.hit_Six()

print(f"Sakib: {sakib.run}")
print(f"Tamim: {tamim.run}")
print(f"Team run: {Player.team_run}")
        
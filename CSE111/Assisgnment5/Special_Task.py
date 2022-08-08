fire_type = "Charmander" , "Cyndaquil"
water_type = "Squirtle" , "Totodile"
grass_type = "Bulbasaur" , "Chikorita"


player1 = input("You choose: ")
player2 = input("Gray chooses")

if player1 in fire_type and player2 in grass_type:
    affinity = 2
    
elif player1 in water_type and player2 in fire_type:
    affinity = 2

elif player1 in grass_type and player2 in water_type:
    affinity = 2
    
elif player1 in fire_type and player2 in water_type:
    
    affinity = 0.5

elif player1 in water_type and player2 in grass_type:
    affinity = 0.5

elif player1 in grass_type and player2 in fire_type:
    affinity = 0.5
    
elif player1 in fire_type and player2 in fire_type:
    
    affinity = 1

elif player1 in water_type and player2 in water_type:
    
    affinity = 1

elif player1 in grass_type and player2 in grass_type:
    
    affinity = 1
    
    

    
    

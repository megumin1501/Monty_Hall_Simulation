import random

def classic_monty_hall_switch():
    doors = [1,2,3]
    car_door = random.choice(doors)
    user_door = random.choice(doors)
      
    remaining_doors = [d for d in doors if d != user_door]
    revealed_door = random.choice(remaining_doors)
    if revealed_door == car_door:
        revealed_door = [d for d in remaining_doors if d != car_door][0]
    user_door = [d for d in remaining_doors if d != revealed_door][0]
    
    if user_door == car_door:
        return 1
    else:
        return 0
    
def classic_monty_hall_no_switch():
    doors = [1,2,3]
    car_door = random.choice(doors)
    user_door = random.choice(doors)
      
    remaining_doors = [d for d in doors if d != user_door]
    revealed_door = random.choice(remaining_doors)
    if revealed_door == car_door:
        revealed_door = [d for d in remaining_doors if d != car_door][0]
        
    if user_door == car_door:
        return 1
    else:
        return 0
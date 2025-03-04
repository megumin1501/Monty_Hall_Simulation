import random

def monty_hall_switch(n):
    doors = [f"door{nth}" for nth in range(1,n+1)]
    car_door = random.choice(doors)
    user_door = random.choice(doors)
    
    remaining_doors = doors.copy()
    remaining_doors.remove(user_door)
    remaining_door = None   
    
    if car_door in remaining_doors:
        remaining_door = car_door
    else:
        remaining_door = random.choice(remaining_doors) 

    user_door = remaining_door
    return (user_door == car_door)

def monty_hall_no_switch(n):
    doors = [d for d in range(1,n+1)]
    car_door = random.choice(doors)
    user_door = random.choice(doors)
    
    return (user_door == car_door)
    
def monty_hall_switch_step_by_step(n):
    doors = ["door" + str(nth) for nth in range(1,n+1)]
    car_door = random.choice(doors)
    user_door = random.choice(doors)
    remaining_doors = [door for door in doors if door != user_door]
    
    number_of_revealed_door = 0
    revealed_doors = []
    while number_of_revealed_door != n-2:
        revealed_door = random.choice(remaining_doors)
        if revealed_door != car_door:
            remaining_doors.remove(revealed_door)
            number_of_revealed_door = number_of_revealed_door + 1
            revealed_doors.append(revealed_doors)
        else:
            continue

    user_door = remaining_doors[0]
    
    if user_door == car_door:
        return 1
    else:
        return 0
    

def monty_hall_no_switchs_step_by_step(n):
    doors = ["door" + str(nth) for nth in range(1,n+1)]
    car_door = random.choice(doors)
    user_door = random.choice(doors)
    remaining_doors = [door for door in doors if door != user_door]
    number_of_revealed_door = 0
    revealed_doors = []
    while number_of_revealed_door != n-2:
        revealed_door = random.choice(remaining_doors)
        if revealed_door != car_door:
            remaining_doors.remove(revealed_door)
            number_of_revealed_door = number_of_revealed_door + 1
            revealed_doors.append(revealed_doors)
        else:
            continue
    
    if user_door == car_door:
        return 1
    else:
        return 0
    

    

for _ in range(1,10):
    monty_hall_switch_step_by_step(10)
    

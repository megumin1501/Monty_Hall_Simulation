import random

# if the player switches
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

# if the player stays
def monty_hall_no_switch(n):
    doors = [d for d in range(1,n+1)]
    car_door = random.choice(doors)
    user_door = random.choice(doors)
    
    return (user_door == car_door)

# Simulate scenarios
def monty_hall_runner(turns, doors):
    switch = {
        'win': 0,
        'lose': 0,
    }
    
    no_switch = {
        'win': 0,
        'lose': 0,
    }

    for _ in range(0,turns):
        res = monty_hall_switch(doors)
        if res == 1 :
            switch['win'] = switch['win'] + 1
        else:
            switch['lose'] = switch['lose'] + 1

    for _ in range(0,turns):
        res = monty_hall_no_switch(doors)
        if res == 1 :
            no_switch['win'] = no_switch['win'] + 1
        else:
            no_switch['lose'] = no_switch['lose'] + 1
    return switch,no_switch
    
# Simulate the 'switch' scenario in the Monty Hall problem step by step, without optimization
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
    
# Simulate the 'stay' scenario in the Monty Hall problem step by step, without optimization
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
    

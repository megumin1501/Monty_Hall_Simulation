import random

def monty_hall_game():
    doors = ['door1', 'door2', 'door3']
    car_door = random.choice(doors)
    
    while True:
        print("Choose your door (1, 2, or 3):")
        user_input = input()
        if user_input in ["1", "2", "3"]:
            user_door = doors[int(user_input) - 1]
            break
        print("Your choice is not valid. Please enter 1, 2, or 3.")
    
    remaining_doors = [d for d in doors if d != user_door]
    revealed_door = random.choice(remaining_doors)
    if revealed_door == car_door:
        revealed_door = [d for d in remaining_doors if d != car_door][0]
    print(f"The host opens {revealed_door} to reveal a goat.")
    
    # Ask if user wants to switch
    while True:
        print("Do you want to switch your door? (yes or no):")
        switch = input()
        if switch in ["yes", "no"]:
            break
        print("Please answer 'yes' or 'no'.")
    
    # If user switches, update their choice to the other unopened door
    if switch == "yes":
        user_door = [d for d in remaining_doors if d != revealed_door][0]
    
    # Show results
    print(f"Your final choice is {user_door}.")
    print(f"The car is behind {car_door}.")
    if user_door == car_door:
        print("Congratulations! You win the car!")
    else:
        print("You lose. Better luck next time!")
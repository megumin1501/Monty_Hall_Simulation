from monty_hall import monty_hall_switch, monty_hall_no_switch
from game import monty_hall_game
from visualize import line_chart

def monty_hall_run(turns, doors):
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
    
def monte_carlo_experiments(turns = 10, doors = 3):
    switch, no_switch = monty_hall_run(turns,doors)
    print(f"\nMonte Carlo Experiments with {turns} turns and {doors} doors")
    print("if player switch :")
    print(f"+ there are {switch['win']} winning turns")
    print(f"+ there are {switch['lose']} losing turns")
    print(f"+ win rate is {round(( switch['win'] / turns ) * 100, 2 )} %")
    print(f"+ ratio win / lose is {round(( switch['win'] / switch['lose'] ), 2 )}")
    print("---------------------------------------------------------------------------------------------")
    print("if player stay : ")
    print(f"+ there are {no_switch['win']} winning turns")
    print(f"+ there are {no_switch['lose']} losing turns")
    print(f"+ win rate is {round(( no_switch['win'] / turns ) * 100, 2)} %")
    print(f"+ ratio win / lose is {round(( no_switch['win'] / no_switch['lose'] ), 2 )}")

def visualize_monte_carlo_experiments():
    switch_results = []
    no_switch_results = []
    for i in range(3,100):
        switch, no_switch = monty_hall_run(100,i)
        switch_results.append(switch['win'])
        no_switch_results.append(no_switch['win'])    
    line_chart(switch_results,no_switch_results)
        
if __name__ == "__main__":
    while True:
        print("\n--- Monty Hall Problem Simulator ---")
        print("1. Play the Monty Hall Game")
        print("2. Run Monte Carlo Experiments")
        print("3. Visualie results")
        print("4. Exit")
        choice = input("Choose an option (1, 2,3 or 4): ").strip()

        if choice == "1":
            print(f"\nMonty Hall Game")
            monty_hall_game()
        elif choice == "2":
            turns = input("Enter the number of turns (default: 10): ").strip()
            doors = input("Enter the number of doors (default: 3): ").strip()
            turns = int(turns) if turns else 10
            doors = int(doors) if doors else 3
            monte_carlo_experiments(turns, doors)
        elif choice == "3":
            visualize_monte_carlo_experiments()
            break
        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

from features.visualize import line_chart
from features.monty_hall import monty_hall_runner

def monte_carlo_experiments(turns = 10, doors = 3):
    switch, no_switch = monty_hall_runner(turns,doors)
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
        switch, no_switch = monty_hall_runner(100,i)
        switch_results.append(switch['win'])
        no_switch_results.append(no_switch['win'])    
    line_chart(switch_results,no_switch_results)

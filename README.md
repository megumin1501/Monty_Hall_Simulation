
# Monty_Hall_Simulation

A simulation of the Monty Hall problem implemented in Python



## What is Monty Hall problem ?
The Monty Hall problem is a famous probability puzzle based on a TV game show. It often confuses people due to its solution.

### Problem statement
You're on a game show, and you're presented with three doors. Behind one of the doors is a car (the prize), while behind the other two doors are goats (non-prizes)

1. You choose one of the three doors (but it is not opened yet)
2. The host, Monty Hall, who knows what’s behind the doors, opens another door that has a goat
3. You are now given a choice : 
+ Stay with your original door.
+ Switch to the remaining closed door

Should you stay or switch to maximize your win rate ? 

### Revelation
The solution reveal that you should switch. If you stay with your original choice, your probability of winning the car is 1/3. If you switch, your probability of winning increases to 2/3.

## About the project
It is a CLI program with 3 main features : 

+ Play the classic Monty Hall with 3 doors
+ Using Monte Carlo method to simulate the Monty Hall problem, with customizable number of doors and turns
+ Visuazlize the win rates of "switch" and "stay" choices using a line chart
## Run the project 
### Prerequisites 
Ensure you have : 
+ Python (version 3.x recommended)
+ numpy and matplotlib 
if they're not installed , you can install them using pip command

    pip install numpy matplotlib
### Clone and Run
To run the project in CLI

    git clone https://github.com/megumin1501/Monty_Hall_Simulation.git
    cd Monty_Hall_Simulation
    python main.py



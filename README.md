
# Monty Hall Simulation

A simulation of the Monty Hall problem using Monte Carlo method implemented in Python 
## What is Monty Hall problem ?
The Monty Hall problem is a famous probability puzzle based on a TV game show. It often confuses people due to its solution.

![Alt text](https://github.com/megumin1501/Monty_Hall_Simulation/blob/main/imgs/mt.png)

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


##  Simulate the problem with Monte Carlo method
The Monte Carlo method is a computational technique that uses random sampling to estimate the result. Instead of solving a problem exactly, Monte Carlo simulations use random numbers to approximate the answer. 

The more the number of simulations increases, the more the estimate converges to the true value

![report](https://github.com/megumin1501/Monty_Hall_Simulation/blob/main/imgs/report.png)

### Code 
A *monty_hall_runner* function simulates the Monte Carlo method and will return the results (number of winnings or losses) in each scenario (switch or stay)

<img src="https://github.com/megumin1501/Monty_Hall_Simulation/blob/main/imgs/mt_runner.png" width="550" height="600"/>

### Result
In the classic Monty Hall problem with 3 doors, if a contestant plays 100 turns:

Visualize the results of the experiment: there are 97 versions of Monty Hall (from 3 doors to 100 doors). Each version is played 100 times. The line chart shows the winning rate of 2 scenarios: "switch" and "no switch".

![chart](https://github.com/megumin1501/Monty_Hall_Simulation/blob/main/imgs/chart.png)

Comments :
+ The winning rate of "switch" is always higher than "no switch"
+ The more doors there are, the more the winning rate for the "switch" option is guaranteed.

from features.game import monty_hall_game
from features.monte_carlo_method import monte_carlo_experiments, visualize_monte_carlo_experiments

if __name__ == "__main__":
    while True:
        print("\n--- Monty Hall Problem Simulator ---")
        print("1. Play the Monty Hall Game")
        print("2. Run Monte Carlo Experiments")
        print("3. Visualie results")
        print("4. Exit")
        choice = input("Choose an option (1,2,3 or 4): ").strip()

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

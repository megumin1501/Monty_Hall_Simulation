import matplotlib.pyplot as plt
import numpy as np
# from main import visualize_monte_carlo_experiments

    
def line_chart(switch_results,no_switch_results):
    x = np.linspace(3, 100, 97) 
    y1 = [result for result in switch_results]
    y2 = [result for result in no_switch_results]

    # Create the plot
    plt.plot(x, y1, label='switch', color='blue', linestyle='-')
    plt.plot(x, y2, label='no switch', color='red', linestyle='--')

    # Add labels and title
    plt.xlabel('Number of doors')
    plt.ylabel('win rate (%)')
    plt.title('Line chart visualize win rate')

    # Add legend
    plt.legend()

    # Show the plot
    plt.show()


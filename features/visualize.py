import matplotlib.pyplot as plt
import numpy as np

def line_chart(switch_results,no_switch_results):
    x = np.linspace(3, 100, 97) 
    y1 = [result for result in switch_results]
    y2 = [result for result in no_switch_results]

    plt.plot(x, y1, label='switch', color='blue', linestyle='-')
    plt.plot(x, y2, label='no switch', color='red', linestyle='--')

    plt.xlabel('Number of doors')
    plt.ylabel('win rate (%)')
    plt.title('Line chart visualize win rate')

    plt.legend()

    plt.show()

import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

# Global variables
fig = None
ax = None
iteration = 0

def run_simulation(event=None):
    #Run or rerun the simulation
    global ax
    
    # Clear the previous plot
    ax.clear()
    
    total_h = 0
    total_t = 0
    
    # Arrays to store values over time
    proportion_array = []  # Actual proportion of heads
    iterations = []
    
    for x in range(1, iteration + 1):
        pick = random.randint(0, 1)
        if pick == 1:
            total_h += 1
        else:
            total_t += 1
        
        # Calculate actual proportion of heads
        current_proportion_h = total_h / x
        proportion_array.append(current_proportion_h)
        iterations.append(x)
    
    # Final averages
    percent = 100/iteration
    avg_h = round((total_h * percent), 3)
    avg_t = round((total_t * percent), 3)
    
    # Print results to console
    print(f"\n--- New Simulation ({iteration} flips) ---")
    print(f"avg_h = {avg_h}%, avg_t = {avg_t}%")
    print(f"Final proportion of heads: {proportion_array[-1]:.4f}")
    
    # Plot the proportion of heads converging to 0.5
    ax.plot(iterations, proportion_array, 'b-', alpha=0.7, label=f'Proportion of Heads (Final: {proportion_array[-1]:.4f})')
    # Add horizontal line at 50% (0.5)
    ax.axhline(y=0.5, color='r', linestyle='--', alpha=0.7, label='Expected 50%')
    
    ax.set_xlabel('Number of Flips')
    ax.set_ylabel('Proportion of Heads')
    ax.set_title(f'Coin Flip Convergence to 0.5 ({iteration} flips)')
    ax.legend()
    ax.grid(True)
    ax.set_ylim(0.0, 1.0)  # Set y-axis from 0.0 to 1.0
    
    # Redraw the plot
    
    plt.draw()

def main():
    global fig, ax, iteration
    
    # Get user input for number of iterations
    iteration = int(input("How many times do you want to flip the coin? "))
    print(f"Looping {iteration} times\n")
    
    # Create figure with button
    fig, ax = plt.subplots(figsize=(10, 6))
    plt.subplots_adjust(bottom=0.2)  # Make room for the button
    
    # Create button axes
    button_ax = plt.axes([0.81, 0.05, 0.15, 0.075])  # [left, bottom, width, height]
    rerun_button = Button(button_ax, 'Rerun Simulation', color='lightblue', hovercolor='0.975')
    
    # Connect button to run_simulation function
    rerun_button.on_clicked(run_simulation)
    
    # Run initial simulation
    run_simulation()
    
    plt.show()

if __name__ == "__main__":
    main()

import random
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

# Global variables
fig = None
ax = None
iteration = 0

def run_simulation(event=None):
    #Run or rerun the dice simulation showing expected value
    global ax
    
    # Clear the previous plot
    ax.clear()
    
    total_sum = 0
    roll_counts = []
    running_averages = []
    expected_value = 3.5
    
    for x in range(1, iteration + 1):
        # Roll the dice (1-6)
        roll = random.randint(1, 6)
        total_sum += roll
        
        # Calculate expected value
        current_average = total_sum / x
        running_averages.append(current_average)
        roll_counts.append(x)
    
    # Print results to console
    print(f"\nSimulation ({iteration} rolls)")
    print(f"Final average: {running_averages[-1]:.4f}")
    print(f"Expected: 3.5")
    print(f"Difference: {abs(running_averages[-1] - expected_value):.4f}")
    
    # Plot the running average with label
    ax.plot(roll_counts, running_averages, 'b-', linewidth=1, label=f'Actual: {running_averages[-1]:.3f}')
    
    # Add horizontal line at expected value 3.5 with label 
    ax.axhline(y=expected_value, color='r', linestyle='-', linewidth=1, label=f'Expected: {expected_value}')
    
    # plot formatting
    ax.set_xlabel('Rolls')
    ax.set_ylabel('Average')
    ax.set_title(f'Dice Average ({iteration} rolls)')
    ax.grid(True, alpha=0.3)
    ax.set_ylim(2.0, 5.0)
    
    # Add key with colors
    ax.legend(loc='upper right')
    
    # Redraw
    plt.draw()

def main():
    global fig, ax, iteration
    
    # Get user input
    iteration = int(input("Number of dice rolls: "))
    print(f"Rolling {iteration} times\n")
    
    # Create figure
    fig, ax = plt.subplots(figsize=(10, 6))
    plt.subplots_adjust(bottom=0.15)
    
    # Create button
    button_ax = plt.axes([0.81, 0.05, 0.15, 0.075])
    rerun_button = Button(button_ax, 'Rerun', color='lightblue')
    
    # Connect button
    rerun_button.on_clicked(run_simulation)
    
    # Run initial simulation
    run_simulation()
    
    plt.show()

if __name__ == "__main__":
    main()

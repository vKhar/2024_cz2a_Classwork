import numpy as np
import matplotlib.pyplot as plt

def show_cluster(contacts):
    data = np.array( contacts.get_array(), dtype=object )
    data[data != None ] = 1
    data[data == None ] = 0

    # Create an array of indices for the x-axis
    indices = np.arange(len(data))

    # Plot the values
    plt.figure(figsize=(10, 2))

    # Plot 'x' for 1 and '' for 0
    for i, value in enumerate(data):
        if value == 1:
            plt.plot(i, 0, 'x', color='blue', markersize = 5)  # Plot 'x' at position i
        else:
            plt.plot(i, 0, '', color='red', markersize=0)  # Plot nothing for 0

    # Set labels and title
    plt.yticks([])  # Hide y-axis ticks
    plt.xlabel('Index')
    plt.title('Occupancy of slots in Hash table')

    # Show the plot
    plt.show()
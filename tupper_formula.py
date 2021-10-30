"""
file:
    tupper_formula.py
author: 
    Thomas Ganley
date:
    2021-10-30
description:
    Code that will take user's input k to display the 106x17 grid from
    {k,k+17} defined by Tupper's self_referential inequality
"""

import matplotlib.pyplot as plt
import matplotlib.colors
import numpy as np

# Define the colormap that we will use for plotting
cmap = matplotlib.colors.ListedColormap(['black', 'white'])

# Define function for Tupper's self-referential formula
# TODO: Implement the actual function
def formula():
    """Tupper's self-referential formula"""
    return np.random.randint(0,2,(17,106))

# Ask user for the k value at which they want to display the grid

# Display the grid
matrix = formula();
print(matrix)
plt.matshow(matrix, cmap=cmap)
plt.show()

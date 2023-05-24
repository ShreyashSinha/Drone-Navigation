import matplotlib.pyplot as plt

# Create some sample data
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

# Create a figure and axis
fig, ax = plt.subplots()

# Plot the data with a specific color
ax.plot(x, y, color='black')

# Show the plot
plt.show()
import matplotlib.pyplot as plt

# Input data
stocks = ['DE', 'GIS', 'MSFT', 'Portfolio']
average_monthly_returns = [-0.32, -1.23, 0.47, -0.36]  # in percentage
standard_deviations = [0.143384047, 0.138648594, 0.143617785, 0.102486631]

# Create a figure and a set of subplots
fig, ax = plt.subplots()

# Plot each stock
for i in range(len(stocks)):
    ax.scatter(standard_deviations[i], average_monthly_returns[i])
    ax.text(standard_deviations[i], average_monthly_returns[i], stocks[i])

# Set labels
ax.set_xlabel('Risk (Standard Deviation)')
ax.set_ylabel('Average Monthly Returns (%)')
ax.set_title('Risk-Return Profile')

# Show the plot
plt.show()

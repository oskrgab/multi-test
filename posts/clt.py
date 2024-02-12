import numpy as np
import matplotlib.pyplot as plt

# Parameters
num_days = 30  # Number of days in a month
hours_per_day = 8  # Bank's operational hours per day

# Generate samples from a Poisson distribution (customer arrivals per hour)
data = np.random.poisson(lam=2, size=(num_days, hours_per_day))

# Calculate the average number of customers per day
daily_averages = np.mean(data, axis=1)

# Plot the distribution of daily averages
plt.hist(daily_averages, bins='auto', density=True, color='lightgreen', alpha=0.7)
plt.title('Distribution of Daily Average Customer Arrivals')
plt.xlabel('Average Number of Customers')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
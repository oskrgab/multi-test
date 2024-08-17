from matplotlib.ticker import EngFormatter
import matplotlib.pyplot as plt

# Sample data: Cumulative oil production
wells = ['Well A', 'Well B', 'Well C', 'Well D']
oil_cumulative = [3.4e6, 7.2e6, 1.2e7, 5.5e6] 

# Create a bar chart
fig, ax = plt.subplots()
ax.bar(wells, oil_cumulative)

formatter = EngFormatter(unit='STB')
formatter.ENG_PREFIXES[6] = "MM"

# Apply engineering notation to y-axis
ax.yaxis.set_major_formatter(formatter)

ax.set_xlabel('Wells')
ax.set_title('Oil Cumulative')

plt.tight_layout()
plt.savefig('eng_formatter/eng_formatter.png', dpi=300)
plt.show()

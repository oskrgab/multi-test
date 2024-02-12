import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull, convex_hull_plot_2d

# Generate some random data
points = np.random.rand(100, 2)

# Compute the convex hull
hull = ConvexHull(points)

# Plot the points and the convex hull
fig, ax = plt.subplots(figsize=(8, 8))
_ = convex_hull_plot_2d(hull, ax=ax)
plt.show()
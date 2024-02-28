import numpy as np
from scipy.stats import norm

# Create a random number generator object using numpy
seed = 28
rng = np.random.default_rng(seed=seed)

# Generate random numbers from a normal distribution and rng object
data = norm.rvs(loc=0, scale=1, size=1000, random_state=rng)



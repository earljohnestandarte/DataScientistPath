import numpy as np

# Create data for 1,000 people
# Average height = 175cm
# Spread (Standard Deviation) = 10cm
heights = np.random.normal(loc=175, scale=10, size=1000)

# Let's check the first 5 people
print(heights[:5])
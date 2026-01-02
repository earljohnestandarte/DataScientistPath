import numpy as np

A = np.array([
    [0, 5, -10],
    [0, 22, 16],
    [0, -9, -2],
])

X = np.array([-5, -4, 3])

print(f"This is Matrix A: {A}")
print(f"This is the input vector X: {X}")


print(f"This is the product of Matrices A and X: {A @ X}")

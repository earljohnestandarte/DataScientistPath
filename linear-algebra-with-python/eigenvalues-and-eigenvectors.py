import numpy as np

A = np.array([[4,1],
              [2,3]
              ])

eigenvalues, eigenvectors = np.linalg.eig(A)

print(f"This are the eigenvectors  of array {A}: {eigenvectors}")
print(f"This are the eigenvalues  of array {A}: {eigenvalues}")
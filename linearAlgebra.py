import numpy as np

a = np.full((3,2),3)
b = np.full((2,3),4)

print(np.matmul(a,b))

# find the determinant
c = np.identity(5)
print(np.linalg.det(c))
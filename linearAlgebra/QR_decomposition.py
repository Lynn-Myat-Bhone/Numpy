import numpy as np

a = np.array([[1,2,3],[4,5,6]])
print(np.linalg.qr(a)) # a = Q * R # Q is othogonal matrix and R is triangular matrix

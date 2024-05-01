# solution for exe1.txt
import numpy as np

a = np.ones((5,5))
b = np.zeros((3,3))
b[1,1] = 9
a[1:4,1:4]=b # a[1 to 3 (row), 1 to 3 (col)]

print(a)
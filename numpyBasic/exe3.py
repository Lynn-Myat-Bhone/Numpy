import numpy as np

z = np.array([[1,2,8,3],
              [4,5,8,6],
              [7,8,9,9]])
# reverse row and col
#       (row),(col)
print(z[::-1,::-1]) # ::-1 is reverse method
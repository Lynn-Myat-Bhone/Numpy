import numpy as np

z = np.array([[0,1,2,3,4],[5,6,7,8,9]])
#min value in 2D array
print(np.min(z))
#min value in row
print(np.min(z,axis=1))
#min value in col
print(np.min(z,axis=0))
# different of min and max values in second axis
print((np.min(z,axis=0)-np.max(z,axis=0)))

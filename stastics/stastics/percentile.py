import numpy as np

z = np.array([[1,2,3],[4,5,6]])
#80th percentile along the second axis

print(np.percentile(z,80,1)) # np.percentile(data,percent,axis)
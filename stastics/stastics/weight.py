import numpy as np

z = np.array([0,1,2,3,4])
weight = np.arange(1,6)

print (np.average(z, weights=weight))  


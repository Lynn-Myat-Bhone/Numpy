import numpy as np
import matplotlib.pyplot as plot
z = np.array([0.5, 0.7, 1.0, 1.2 ,1.3, 2.1])
b = np.array([0,1,2,3])
# hist is only for numerical data
plot.hist(z,bins = b) # bins provided the ege of histogram data 
plot.show()
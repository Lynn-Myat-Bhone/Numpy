import numpy as np

#centigrade
a = np.array([0,12,45.21,34,99.91])

# convert to fahrenheit
print(np.round((9*a +(32*5))/2,3)) #round(input data, decimal) decimal count start from zero
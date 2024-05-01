import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# read file witk pandas

data = pd.read_csv('Auto.csv')

# using matplotlib to draw graph

fig,ax = plt.subplots(figsize =(8,8))
ax.plot(data['person'],data['age'])

ax.set_title("Perosn and Age")
plt.xlabel("Person")
plt.ylabel("Age")

# display
print(data.describe()) #count, mean, standard deviation, minimum value, maximum value, and quartile information.
plt.show()
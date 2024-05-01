import pandas as pd
import numpy as np
import matplotlib.pyplot as plot

data = pd.read_csv('Auto.csv')
print(data)
print (data.columns)
# print(data['person'])
# sum = data['age'].sum()
# print(f"sum fo all age: {sum}")
print (data['age']<10)

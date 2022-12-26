import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Read in CSV file
df = pd.read_csv("snowpit.csv")
# s = df.shape
# print(s)
# print(df.columns)
# print(df["thickness"])
# print(df["hardness"])

# Split data into categories
thickness = df["thickness"]
hardness = df["hardness"] 
type = df["grain type"] 
size = df["grain size"] 
humidity = df["humidity"] 
temperature = df["temperature"] 

max_depth = -sum(thickness)
y_ax = np.linspace(0, max_depth,-max_depth)
x_ax = []

s = 0
index = 0
for i in thickness:
    for j in range( s, s+i):
        x_ax.append(hardness[index])
    index += 1
    s += i

x_ax[0] = " "

sns.set_theme(style = "dark")
plt.title("Snowpit profile")
plt.plot(x_ax,y_ax)
plt.plot(hardness, temperature)
plt.xlabel("[mm]")
plt.show()

# Plotting
sns.histplot(data = df, x="hardness", y="thickness")

plt.show()

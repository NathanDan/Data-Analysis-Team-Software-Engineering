from matplotlib import pyplot as plt
from matplotlib import style
import pandas as pd


df20 = pd.read_csv('Berlin 2020.csv', parse_dates=['Month'], index_col="Month")

df19 = pd.read_csv('Berlin 2019.csv', parse_dates=['Month'], index_col="Month")

ax = df20.plot(color='#3498db')
ax.set_ylabel("NO2 Level")
df19.plot(color='#d5d8dc', title='Difference In NO2 Levels In 2019 And 2020 - Berlin',ax=ax)

plt.plot()
plt.show()


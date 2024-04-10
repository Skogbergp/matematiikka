from matplotlib import pyplot as plt,patches
import numpy as np
from fractions import Fraction as fr

import matplotlib as mpl




fig = plt.figure(figsize=(19.2,14.4))
ax = fig.subplots()

ymp = patches.Circle((0,0),radius=1,fill=0)
ax.add_patch(ymp)

ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.axis('equal')

#
plt.xticks([-1, 0, 1], minor=True)
plt.yticks([-1, 0, 1])

varit=np.array(['red', 'green', 'blue', 'orange'])

pisteet = np.array([30, 45, 60, 90, 120, 150, 180, 270])

radpisteet = np.radians(pisteet)
x = np.cos(radpisteet)
y = np.sin(radpisteet)

plt.scatter(x, y, marker='o')

for i in range(len(pisteet)):
    plt.annotate(str(pisteet[i]),
             xy=(np.cos(radpisteet[i]), np.sin(radpisteet[i])), xycoords='data',
             xytext=(+30, +5), textcoords='offset points', fontsize=12,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0"))

plt.show()

import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(3*(-np.pi), 3*np.pi, 256, endpoint=True)
C,S = np.cos(X), np.sin(X)

plt.figure(figsize=(19,13))
plt.plot(X,C,color="orange")
plt.plot(X,S,color="teal")

plt.xticks([3*-np.pi, 3*-np.pi/2, 0, 3*np.pi/2,3* np.pi],
       [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])

plt.yticks([-1, 0, +1],
       [r'$-1$', r'$0$', r'$+1$'])


plt.show()
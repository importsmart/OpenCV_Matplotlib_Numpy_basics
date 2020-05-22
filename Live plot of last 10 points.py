import numpy as np
import matplotlib.pyplot as plt

randx = np.random.randint(0,100,50)
randy = np.random.randint(0,100,50)

for i in range(50):
    if(i<10):
        plt.scatter(randx[i], randy[i],color='blue')
        plt.pause(1)
    else:
        plt.clf()
        plt.scatter(randx[i-10:i], randy[i-10:i],color='blue')
        plt.pause(1)

plt.show()
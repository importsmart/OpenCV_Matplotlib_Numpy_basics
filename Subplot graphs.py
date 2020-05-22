import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import norm


mean = [0,4,-3.5]
var = [5, 0.2, 0.05]
col = ['b','g','r']
legend = ['upper right','upper left','upper right']

dom1 = np.linspace(-10,10,1000)
dom2 = np.linspace(3,5,1000)
dom3 = np.linspace(-4,-3,1000)
dom = [dom1,dom2,dom3]

for i in range(3):
    plt.subplot(3, 1, i+1)
    plt.plot(dom[i], norm.pdf(dom[i], mean[i], var[i]), col[i], label='mean={0}, var={1}'.format(mean[i],var[i]))
    plt.legend(loc=legend[i])
    plt.xlabel("Value")
    plt.ylabel("Density")

plt.show()
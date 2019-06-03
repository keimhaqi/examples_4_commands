import matplotlib
import numpy as np
import matplotlib.pyplot as plt

x = range(1, 11)

fig, ax = plt.subplots()

n, bins, patches = ax.hist(x, 20)

plt.show()
import matplotlib.pyplot as plt
import numpy as np

# fig = plt.figure()
# print fig
# fig.suptitle('No axes on this figure')
# fig2, ax_lst = plt.subplots(2, 2)

# print fig2, ax_lst

x = np.linspace(0, 2, 100)

plt.plot(x, x, label='linear')
plt.plot(x, x ** 2, label='quadratic')
plt.plot(x, x ** 3, label='cubic')

plt.xlabel('x label')
plt.ylabel('y label')

plt.title("Simple Plot")

plt.legend()

plt.show()
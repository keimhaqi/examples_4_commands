import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

# fig = plt.figure()
# print fig
# fig.suptitle('No axes on this figure')
# fig2, ax_lst = plt.subplots(2, 2)

# print fig2, ax_lst

# x = np.linspace(0, 2, 100)

# plt.plot(x, x, label='linear')
# plt.plot(x, x ** 2, label='quadratic')
# plt.plot(x, x ** 3, label='cubic')

# plt.xlabel('x label')
# plt.ylabel('y label')

# plt.title("Simple Plot")

# plt.legend()

# plt.show()

# plt.ion()
# plt.plot([1.6, 2.7])

# plt.title("interactive test")
# plt.xlabel("index")

# ax = plt.gca()
# ax.plot([3.1, 2.2])
# plt.draw()

# plt.ioff()
# plt.plot([1.6, 2.7])
# plt.show()

# plt.ioff()
# for i in range(3):
#     plt.plot(np.random.rand(10))
#     plt.show()

# y = np.random.rand(100000)
# y[50000:] *= 2
# y[np.logspace(1, np.log10(50000), 400).astype(int)] = -1
# mpl.rcParams['path.simplify'] = True

# mpl.rcParams['path.simplify_threshold'] = 0.0
# plt.plot(y)
# plt.show()

# mpl.rcParams['path.simplify_threshold'] = 1.0
# plt.plot(y)
# plt.show()

plt.plot(x, y, markevery = 10)
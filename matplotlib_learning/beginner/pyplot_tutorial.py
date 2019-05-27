import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter
import numpy as np
# plt.plot([1,2,3,4])
# plt.ylabel('some numbers')
# plt.show()
# plt.plot([1,2,3,4],[1,4,9,16])
# plt.ylabel('some numbers')
# plt.show()

# plt.plot([1,2,3,4], [1,4,9,16], 'g^')
# plt.axis([0, 6, 0, 20])
# plt.show()


# t = np.arange(0., 5., 0.2)
# plt.plot(t, t, 'r--', t, t ** 2, 'bs', t, t ** 3, 'g^')
# plt.show()

# data = {
#     'a': np.arange(50),
#     'c': np.random.randint(0, 50, 50),
#     'd': np.random.randn(50)
# }

# data['b'] = data['a'] + 10 * np.random.randn(50)
# data['d'] = np.abs(data['d']) * 100
# plt.scatter('a', 'b', c = 'c', data=data)
# plt.xlabel('entry a')
# plt.ylabel('entry b')
# plt.show()

# names = ['group_a', 'group_b', 'group_c']
# values = [1, 10, 100]

# plt.figure(figsize=(9, 3))
# plt.subplot(131)
# plt.bar(names, values)
# plt.subplot(132)
# plt.scatter(names, values)
# plt.subplot(133)
# plt.plot(names, values)
# plt.suptitle('Categorical Plotting')
# plt.show()

# def f(t):
#     return np.exp(-t) * np.cos(2 * np.pi * t)

# t1 = np.arange(0.0, 5.0, 0.1)
# t2 = np.arange(0.0, 5.0, 0.02)

# plt.figure()
# plt.subplot(221)
# plt.plot(t1, f(t1), 'bo', t2, f(t2), "k")

# # plt.subplot(222)
# # plt.plot(t2, np.cos(2 * np.pi * t2), 'r--')

# # plt.subplot(223)
# # plt.plot(t2, np.cos(2 * np.pi * t2), 'r--')

# # plt.subplot(224)
# # plt.plot(t2, np.cos(2 * np.pi * t2), 'r--')

# plt.show()

# plt.figure(1)
# plt.subplot(211)
# plt.plot([1,2,3])
# plt.subplot(212)
# plt.plot([4,5,6])

# plt.figure(2)
# plt.plot([4,5,6])

# plt.figure(1)
# plt.subplot(211)
# plt.title('Easy as 1, 2, 3')

# plt.show()

# mu, sigma = 100, 15
# x = mu + sigma * np.random.randn(10000)

# # the histogram of the data
# n, bins, patches = plt.hist(x, 50, density=1, facecolor='g', alpha=0.75)

# plt.xlabel("Smarts")
# plt.ylabel("Probability")
# plt.title("Histogram of IQ")
# plt.text(60, .025, r'$\mu=100, \ \sigma=15$')
# plt.axis([40, 160, 0, 0.03])
# plt.grid(True)
# plt.show()

# ax = plt.subplot(111)

# t = np.arange(0.0, 5.0, 0.01)
# s = np.cos(2 * np.pi * t)
# line, = plt.plot(t, s, lw=2)
# plt.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
# arrowprops=dict(facecolor='black', shrink=0.05))
# plt.ylim(-2, 2)
# plt.show()


np.random.seed(19680801)

y = np.random.normal(loc=0.5, scale=0.4, size=1000)
y = y[(y > 0) & (y < 1)]
y.sort()
x = np.arange(len(y))

plt.figure()

plt.subplot(221)
plt.plot(x, y)
plt.yscale('linear')
plt.title('linear')
plt.grid(True)

plt.subplot(222)
plt.plot(x, y)
plt.yscale('log')
plt.title('log')
plt.grid(True)

plt.subplot(223)
plt.plot(x, y - y.mean())
plt.yscale('symlog', linthreshy=0.01)
plt.title('symlog')
plt.grid(True)

plt.subplot(224)
plt.plot(x, y)
plt.yscale('logit')
plt.title('logit')
plt.grid(True)

# plt.gca().yaxis.set_minor_formatter(NullFormatter())
plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25, wspace=0.35)
plt.show()
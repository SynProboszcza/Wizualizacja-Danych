import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from matplotlib import cm

#Zad1

# fig = plt.figure()
# ax = fig.gca(projection='3d')
#
# z = np.linspace(0, 2*np.pi, 100)
# x = np.sin(z)
# y = 2*np.cos(z)
#
# ax.plot(x, y, z)
# plt.show()

#Zad2

# np.random.seed(18912837)
#
# def randrange(n, vmin, vmax):
#     return (vmax - vmin) * np.random.rand(n) + vmin
#
# fig = plt.figure()
# ax = fig.add_subplot(projection='3d')
# n = 100
#
# for c, m, zlow, zhigh in [('tan', '.', 1, 2),('indigo', '1', 3, 4),('mediumturquoise', '*', 5, 6),('aquamarine', '*', 7, 8),('lime', '*', 9, 10)]:
#     xs = randrange(n, 23, 32)
#     ys = randrange(n, 0, 100)
#     zs = randrange(n, zlow, zhigh)
#     ax.scatter(xs, ys, zs, c=c, marker=m)
#
# ax.set_xlabel('x')
# ax.set_ylabel('y')
# ax.set_zlabel('z')
#
# plt.show()

#Zad3

# fig = plt.figure()
# ax = fig.gca(projection='3d')
#
# X = np.arange(-5, 5, 0.25)
# Y = np.arange(-5, 5, 0.25)
# X, Y = np.meshgrid(X, Y)
# R = np.sqrt(X**2 + Y**2)
# Z = np.sin(R)
#
# #lista kolorów do wylosowania
# #losuje żeby nie powtarzać kodu 5 razy
# kolorki = [cm.prism, cm.ocean, cm.terrain, cm.brg, cm.jet]
#
# surf = ax.plot_surface(X, Y, Z, cmap=kolorki[np.random.randint(0,len(kolorki)-1)], linewidth=0, antialiased=False)
#
# ax.set_zlim(-1.01, 1.01)
# ax.zaxis.set_major_locator(LinearLocator(10))
# ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
#
# fig.colorbar(surf, shrink=0.5, aspect=5)
# plt.show()




















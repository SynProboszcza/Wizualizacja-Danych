import matplotlib.pyplot as plt
import numpy as np

#Zad1
# tab = [1/x for x in range(20,41)]
# plt.plot(tab, label="1/x")
# plt.legend()
# plt.xlabel("x")
# plt.ylabel("f(x)")
# plt.ylim(ymin=0.02)
# plt.show()

#Zad2

# tab = [1/x for x in range(20,41)]
# plt.plot(tab, "b--", tab, "bo")
# plt.title("Wykres funckji f(x) dla x[20,40]")
# plt.xlabel("x")
# plt.ylabel("1/x")
# plt.margins(0)
# plt.ylim(ymin=0.02)
# plt.show()

#Zad3

# tab_sin = [np.sin(x) for x in np.linspace(0,46,460)]
# tab_cos = [np.cos(x) for x in np.linspace(0,46,460)]
# plt.subplot(2,1,1)
# plt.plot(tab_sin, label="sin(x)")
# plt.ylabel("y")
# plt.xlabel("x")
# plt.legend()
# plt.subplot(2,1,2)
# plt.plot(tab_cos, label="cos(x)")
# plt.xlabel("x")
# plt.ylabel("y")
# plt.legend()
# plt.show()

#Zad4

# tab_sin = [np.sin(x) for x in np.linspace(0,46,460)]
# tab_sin2 = [np.sin(x)+2 for x in np.linspace(46,0,460)]
# plt.plot(tab_sin2, "orange", label="sin(x)")
# plt.plot(tab_sin, "blue", label="sin(x)")
# plt.xlabel("x")
# plt.ylabel("y")
# plt.legend()
# plt.show()

#Zad5










from matplotlib import pyplot as plt
import math

def f(x):
    A = 3
    B = 3
    return A*math.sin(x) + B*math.cos(x)

xs = []
for i in range (-500, 500):
    xs.append(i*0.01)

ys_seno = []
ys_coseno = []
ys_combinazione = []
for x in xs:
    ys_seno.append(math.sin(x))
    ys_coseno.append(math.cos(x))
    ys_combinazione.append(f(x))


plt.grid()
plt.axhline()
plt.axvline()
plt.plot(xs, ys_seno, linestyle=':', label="sin(x)")
plt.plot(xs, ys_coseno, label="cos(x)")
plt.plot(xs, ys_combinazione, label="combina(x)")
plt.legend()
plt.show()


from math import sin
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def betterSin(x, accuracy):
    a = (-1) ** 0 * x ** 1 / (1)
    sum_a = a

    t = np.arange(0.0, 3.0, 0.01)
    s = np.sin(t*np.pi/2)

    fig, ax = plt.subplots()
    # Original Function
    ax.plot(t,s, label="Sin(x) value")

    # k = 0
    ax.plot(t - sum_a, s, label=0)
    t -= sum_a

    # Cycle through other k's
    for k in range(1, accuracy + 1):
        a = a * ((-1)**k / (2*k*2*k+1)) * x**2
        sum_a += a
        ax.plot(t + sum_a, s, label=k)

    ax.set(xlabel = "x", ylabel = "y", title = "Approximation of Sin")
    ax.legend()
    plt.grid()
    plt.show()
    print("My sin:", sum_a)
    return sum_a

x = 0.75
k = 5
#x = float(input("Enter X value: "))
#k = int(input("Enter accuracy (k) of sin function: "))

print("Real sin:", sin(x))
betterSin(x, k)

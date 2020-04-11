from math import sin
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def betterSin(x, accuracy):
    a = (-1) ** 0 * x ** 1 / (1)
    s = a
    list_s = []
    list_k = []
    list_s.append(s)
    list_k.append(0)
    fig, ax = plt.subplots()
    for k in range(1, accuracy + 1):
        a = a * (-1) ** k / (2 * k * 2 * k + 1) * x ** 2
        s += a
        list_s.append(s)
        list_k.append(k)
    print("My sin:", s)
    ax.plot(list_k, list_s, label="Sin(x) value")
    ax.set(xlabel = "K-values", ylabel = "S-values", title = "Approximation of Sin")
    ax.legend()
    plt.grid()
    plt.show()
    return s

x = 0.9
k = 5
x = float(input("Enter X value: "))
k = int(input("Enter accuracy (k) of sin function: "))

print("Real sin:", sin(x))
betterSin(x, k)

import random
import matplotlib.pyplot as plt
import numpy as np

# define x and y
X = [1, 2, 3, 4, 5]
Y = [5, 7, 9, 11, 13]

# asume initial value for w and b as 0
w_gd, b_gd = 0, 0

# define alpha value
alpha_gd = 0.01

# minumum cost to stop fitting
minimum_cost = 0.01

# y = wx + b
def f(x, w, b):
    return w * x + b

# cost function
def cost(x, y):
    global w_gd
    global b_gd
    w = w_gd
    b = b_gd
    differences = 0
    m = len(x)
    for i in range(len(x)):
        difference = f(x[i], w, b) - y[i]
        differences += pow(difference, 2)
    return (1 / 2 * m) * differences

# calculate new w
def w_new(x, y, alpha):
    global w_gd
    global b_gd
    w = w_gd
    b = b_gd
    differences = 0
    m = len(x)
    for i in range(len(x)):
        difference = f(x[i], w, b) - y[i]
        differences += difference * x[i]
    return w - (alpha * (1 / m) * differences)

# calculate new b
def b_new(x, y, alpha):
    global w_gd
    global b_gd
    w = w_gd
    b = b_gd
    differences = 0
    m = len(x)
    for i in range(len(x)):
        difference = f(x[i], w, b) - y[i]
        differences += difference
    return b - (alpha * (1 / m) * differences)

# fit data until reaching minimum cost
def runner():
    global w_gd
    global b_gd
    counter = 1
    current_cost = cost(X, Y)
    dif_b = 1
    dif_w = 1
    print(counter, ") w =", w_gd, "\tb =", b_gd, "\tcost =", current_cost)
    while current_cost > minimum_cost and (dif_b != 0 or dif_w != 0):
        w_gd_new = w_new(X, Y, alpha_gd)
        b_gd_new = b_new(X, Y, alpha_gd)
        dif_w = abs(w_gd - w_gd_new)
        dif_b = abs(b_gd - b_gd_new)
        print(counter, ") w =", w_gd, "\tb =", b_gd, "\tcost =", current_cost, "\tdif-w =", dif_w, "\tdif-b =", dif_b)
        w_gd = w_gd_new
        b_gd = b_gd_new
        current_cost = cost(X, Y)
        counter += 1

runner()
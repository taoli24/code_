# multiple linear regression with normalization


import numpy as np
from house_data import X_train, y_train

b_init = 0
w_init = np.zeros(4)


def z_score_normalize(x):
    sigma = np.std(x)
    miu = np.mean(x)

    return (x - miu) / sigma


def compute_cost(x, y, w, b):
    m = x.shape[0]
    cost = 0
    for i in range(m):
        f_w_b_i = np.dot(x[i], w) + b
        cost += (f_w_b_i - y[i]) ** 2

    return cost / (2 * m)


def compute_gradient(x, y, w, b):
    m, n = x.shape
    dj_dw = np.zeros(n)
    dj_db = 0

    for i in range(m):
        f_w_b_i = np.dot(x[i], w) + b
        err = f_w_b_i - y[i]
        for j in range(n):
            dj_dw[j] += err * x[i, j]
        dj_db += err

    return dj_dw / m, dj_db / m


def gradient_descent(x, y, w, b, alpha, number_iters, cost_function, gradient_function):
    w, b = w, b
    j_hist, p_hist = [], []

    for i in range(number_iters):
        dj_dw, dj_db = gradient_function(x, y, w, b)
        w -= dj_dw * alpha
        b -= dj_db * alpha

        if i < 10000:
            p_hist.append((w, b))
            j_hist.append(cost_function(x, y, w, b))

        if i % (number_iters // 10) == 0:
            print(f"Iteration {i:4}: Cost: {j_hist[-1]:8.2f} ",
                  f"w1: {w[0]:8.2f} w2: {w[1]:8.2f} w3: {w[2]:8.2f} w4: {w[3]:8.2f}",
                  f"b: {b:8.2f}")

    return w, b, j_hist, p_hist


x_norm = z_score_normalize(x=X_train)
gradient_descent(x_norm, y_train, w_init, b_init, 0.3, 10000, compute_cost, compute_gradient)

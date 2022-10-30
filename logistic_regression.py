# To demonstrate how logistic regression works
# logistic regression is used for binary classification despite its name contains regression
import numpy as np

X_train = np.array([[0.5, 1.5], [1, 1], [1.5, 0.5], [3, 0.5], [2, 2], [1, 2.5]])
y_train = np.array([0, 0, 0, 1, 1, 1])

w_init = np.array([0, 0])
b_init = 0


def z_score_normalisation(x):
    sigma = np.std(x)
    miu = np.mean(x)
    x_normed = (x - miu) / sigma
    return x_normed


def sigmoid_function(z):
    """
    :param z: vector
    :return: vector of sigmoid result
    """
    result = 1 / (1 + np.exp(-z))
    return result


def compute_cost(x, y, w, b):
    m = x.shape[0]
    cost = 0
    for i in range(m):
        z = np.dot(x[i], w) + b
        f_w_b_i = sigmoid_function(z)
        cost += y[i] * np.log(f_w_b_i) + (1 - y[i]) * np.log(1 - f_w_b_i)
    return -cost / m


def compute_gradient(x, y, w, b):
    m, n = x.shape
    dj_dw = np.zeros(n)
    dj_db = 0

    for i in range(m):
        z = np.dot(x[i], w) + b
        f_w_b_i = sigmoid_function(z)
        error = f_w_b_i - y[i]
        dj_db += error
        for j in range(n):
            dj_dw[j] += error * x[i, j]

    return dj_dw/m, dj_db/m


def gradient_descent(x, y, w, b, alpha, n_iters, cost_function, gradient_function):
    w, b = w, b
    j_hist, p_hist = [], []

    for i in range(n_iters):
        dj_dw, dj_db = gradient_function(x, y, w, b)
        w = w - alpha * dj_dw
        b = b - alpha * dj_db

        # prevent resource exhaustion
        if i < 10000:
            j_hist.append(cost_function(x, y, w, b))
            p_hist.append((w, b))

        if i % (n_iters // 10) == 0:
            print(f"Iteration {i:4}: Cost: {j_hist[-1]:8.3f}")

    return w, b, j_hist, p_hist


# print(compute_gradient(X_train, y_train, w_init, b_init))
X_norm = z_score_normalisation(X_train)
gradient_descent(X_norm, y_train, w_init, b_init, 0.1, 10000, compute_cost, compute_gradient)

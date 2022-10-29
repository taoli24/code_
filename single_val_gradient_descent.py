# The purpose is to demonstrate how gradient descent works with single variable
import numpy as np

X_train = np.array([1, 2])
y_train = np.array([2, 5])

# setting initial slope and intercept
init_w, init_b = 0, 0


# define cost function
def single_val_cost_fn(x, y, w, b):
    m = x.shape[0]
    cost = 0

    for i in range(m):
        y_pred = w * x[i] + b
        err = y_pred - y[i]
        cost += err ** 2
    return cost / (2 * m)


# define gradient function
def cal_gradient(x, y, w, b):
    m = x.shape[0]
    dj_dw, dj_db = 0, 0

    for i in range(m):
        err = (w * x[i] + b) - y[i]
        dj_dw += err * x[i]
        dj_db += err

    return dj_dw / m, dj_db / m


# define gradient descent function
def gradient_descent(x, y, in_w, in_b, alpha, num_iters, cost_fn, gradient_fn):
    j_hist, p_hist = [], []
    w, b = in_w, in_b

    for i in range(num_iters):
        # calculate gradient and update parameters
        dj_dw, dj_db = gradient_fn(x, y, w, b)
        w -= dj_dw * alpha
        b -= dj_db * alpha

        # prevent resource exhaustion
        if i < 100000:
            j_hist.append(cost_fn(x, y, w, b))
            p_hist.append((w, b))

        if i % (num_iters // 10) == 0:
            print(f"Iterations {i:4}: Cost: {j_hist[-1]:.2e} ",
                  f"dj_dw: {dj_dw:.3e} dj_db: {dj_db:.3e}",
                  f"w: {w:.3e} b: {b:.3e}")

    return w, b, j_hist, p_hist


gradient_descent(X_train, y_train, init_w, init_b, 0.05, 10000, single_val_cost_fn, cal_gradient)

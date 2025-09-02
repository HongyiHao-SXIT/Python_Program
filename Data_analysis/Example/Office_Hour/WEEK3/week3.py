import numpy as np
import matplotlib.pyplot as plt
from multiprocessing import Pool
import time

def polynomial_loss(theta, X, y):
    m = len(y)
    h = np.dot(X, theta)
    loss = np.sum((h - y) ** 2) / (2 * m)
    return loss

def plot_loss_contour(X, y, theta_history, theta_range=(-10, 10)):
    theta0_vals = np.linspace(theta_range[0], theta_range[1], 100)
    theta1_vals = np.linspace(theta_range[0], theta_range[1], 100)
    theta0_mesh, theta1_mesh = np.meshgrid(theta0_vals, theta1_vals)
    loss_vals = np.zeros_like(theta0_mesh)
    for i in range(len(theta0_vals)):
        for j in range(len(theta1_vals)):
            theta = np.array([theta0_mesh[i, j], theta1_mesh[i, j]])
            loss_vals[i, j] = polynomial_loss(theta, X, y)
    plt.figure(figsize=(8, 6))
    plt.contour(theta0_mesh, theta1_mesh, loss_vals, levels=20, cmap='jet')
    for i in range(len(theta_history) - 1):
        plt.plot(theta_history[i][0], theta_history[i][1], 'bo-', alpha=0.4, linewidth=.5, markersize=2)
    plt.plot(theta_history[-1][0], theta_history[-1][1], 'ro-', alpha=0.8, linewidth=.5, markersize=2)
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.xlabel('theta0')
    plt.ylabel('theta1')
    plt.title('Contour of Loss Function')
    plt.colorbar()
    plt.show()

def stochastic_gradient_descent(args):
    X, y, theta = args
    m = len(y)
    h = np.dot(X, theta)
    error = h - y
    gradient = np.dot(X.T, error) / m
    return gradient

def synchronized_distributed_sgd(X, y, batch_size, learning_rate, num_iterations, num_workers):
    m, n = X.shape
    theta = np.zeros(n)
    theta_history = [theta.copy()]
    start_time = time.time()

    for iter in range(num_iterations):
        with Pool(processes=num_workers) as pool:
            args_list = []
            for _ in range(num_workers):
                index = np.random.choice(len(X), batch_size // num_workers)
                X_batch = X[index, :]
                y_batch = y[index]
                args_list.append((X_batch, y_batch, theta))
            grad_list = pool.map(stochastic_gradient_descent, args_list)
            avg_gradient = np.mean(grad_list, axis=0)
            theta = theta - learning_rate * avg_gradient
            theta_history.append(theta.copy())
        if (iter + 1) % 10 == 0:
            loss = polynomial_loss(theta, X, y)
            print(f"Epoch {iter+1}: Loss = {loss:.4f}")

    time_cost = time.time() - start_time
    print(f"Total Training Time: {time_cost:.2f} seconds")
    return theta, theta_history

def main():
    np.random.seed(0)
    X = np.random.rand(1000, 2)
    y = 7 * X[:, 0] + 1 * X[:, 1] + 1*np.random.randn(1000)

    batch_size = 200
    learning_rate = 0.1
    num_iterations = 100
    num_workers = 4

    theta, theta_history = synchronized_distributed_sgd(X, y, batch_size, learning_rate, num_iterations, num_workers)
    plot_loss_contour(X, y, theta_history)

if __name__ == '__main__':
    main()

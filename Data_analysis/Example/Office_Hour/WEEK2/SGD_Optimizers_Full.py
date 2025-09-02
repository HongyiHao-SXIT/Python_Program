import numpy as np
import matplotlib.pyplot as plt

def polynomial_loss(theta, X, y):
    m = len(y)
    h = np.dot(X, theta)
    loss = np.sum((h - y) ** 2) / m
    return loss

def stochastic_batch_gradient_descent(X, y, batch_size, learning_rate, num_epochs):
    m, n = X.shape
    theta = np.zeros(n)
    theta_history = [theta.copy()]
    num_batches = m // batch_size
    for epoch in range(num_epochs):
        indices = np.random.permutation(m)
        X = X[indices]
        y = y[indices]
        for batch in range(num_batches):
            start_index = batch * batch_size
            end_index = start_index + batch_size
            X_batch = X[start_index:end_index, :]
            y_batch = y[start_index:end_index]
            h_batch = np.dot(X_batch, theta)
            error_batch = h_batch - y_batch
            gradient = np.dot(X_batch.T, error_batch) / batch_size
            theta = theta - learning_rate * gradient
            theta_history.append(theta.copy())
    return theta, theta_history

def momentum_sgd(X, y, batch_size, learning_rate, num_epochs, momentum=0.9):
    m, n = X.shape
    theta = np.zeros(n)
    velocity = np.zeros(n)
    theta_history = [theta.copy()]
    num_batches = m // batch_size
    for epoch in range(num_epochs):
        indices = np.random.permutation(m)
        X = X[indices]
        y = y[indices]
        for batch in range(num_batches):
            start = batch * batch_size
            end = start + batch_size
            X_batch = X[start:end]
            y_batch = y[start:end]
            error = np.dot(X_batch, theta) - y_batch
            gradient = np.dot(X_batch.T, error) / batch_size
            velocity = momentum * velocity - learning_rate * gradient
            theta += velocity
            theta_history.append(theta.copy())
    return theta, theta_history

def adam_optimizer(X, y, batch_size, learning_rate, num_epochs, beta1=0.9, beta2=0.999, epsilon=1e-8):
    m, n = X.shape
    theta = np.zeros(n)
    m_t = np.zeros(n)
    v_t = np.zeros(n)
    theta_history = [theta.copy()]
    num_batches = m // batch_size
    for epoch in range(1, num_epochs + 1):
        indices = np.random.permutation(m)
        X = X[indices]
        y = y[indices]
        for batch in range(num_batches):
            start = batch * batch_size
            end = start + batch_size
            X_batch = X[start:end]
            y_batch = y[start:end]
            error = np.dot(X_batch, theta) - y_batch
            gradient = np.dot(X_batch.T, error) / batch_size

            m_t = beta1 * m_t + (1 - beta1) * gradient
            v_t = beta2 * v_t + (1 - beta2) * (gradient ** 2)
            m_hat = m_t / (1 - beta1 ** epoch)
            v_hat = v_t / (1 - beta2 ** epoch)

            theta = theta - learning_rate * m_hat / (np.sqrt(v_hat) + epsilon)
            theta_history.append(theta.copy())
    return theta, theta_history

def newton_method(X, y, num_epochs=10):
    m, n = X.shape
    theta = np.zeros(n)
    theta_history = [theta.copy()]
    for epoch in range(num_epochs):
        h = np.dot(X, theta)
        error = h - y
        gradient = np.dot(X.T, error) / m
        hessian = np.dot(X.T, X) / m
        update = np.linalg.pinv(hessian).dot(gradient)
        theta = theta - update
        theta_history.append(theta.copy())
    return theta, theta_history

def plot_loss_contour(X, y, theta_history, title='Loss Contour', theta_range=(-1, 10)):
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
    theta_history = np.array(theta_history)
    plt.plot(theta_history[:, 0], theta_history[:, 1], 'bo-', alpha=0.4, linewidth=0.5, markersize=2)
    plt.plot(theta_history[-1, 0], theta_history[-1, 1], 'ro', markersize=5)
    plt.xlabel('theta0')
    plt.ylabel('theta1')
    plt.title(title)
    plt.colorbar(label='Loss')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    np.random.seed(0)
    X = np.random.rand(100, 2)

    y_low_noise = 7 * X[:, 0] + 1 * X[:, 1] + 0.01 * np.random.randn(100)
    theta, history = stochastic_batch_gradient_descent(X, y_low_noise, batch_size=5, learning_rate=0.1, num_epochs=100)
    plot_loss_contour(X, y_low_noise, history, title='SGD - Low Noise')

    y_high_noise = 7 * X[:, 0] + 1 * X[:, 1] + 10 * np.random.randn(100)
    theta, history = stochastic_batch_gradient_descent(X, y_high_noise, batch_size=1, learning_rate=0.01, num_epochs=100)
    plot_loss_contour(X, y_high_noise, history, title='SGD - High Noise')

    theta, history = momentum_sgd(X, y_low_noise, batch_size=5, learning_rate=0.1, num_epochs=100)
    plot_loss_contour(X, y_low_noise, history, title='Momentum SGD - Low Noise')

    theta, history = adam_optimizer(X, y_low_noise, batch_size=5, learning_rate=0.1, num_epochs=100)
    plot_loss_contour(X, y_low_noise, history, title='Adam - Low Noise')

    theta, history = newton_method(X, y_low_noise, num_epochs=10)
    plot_loss_contour(X, y_low_noise, history, title='Newton Method - Low Noise')

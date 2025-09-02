from multiprocessing import Pool
import numpy as np

def compute_gradient(worker_data):
    X_worker, y_worker, theta, batch_size = worker_data
    worker_sample_size = len(X_worker)
    effective_batch_size = min(batch_size, worker_sample_size)
    indices = np.random.choice(worker_sample_size, effective_batch_size, replace=False)
    X_batch = X_worker[indices]
    y_batch = y_worker[indices]
    X_batch_with_bias = np.hstack((X_batch, np.ones((len(X_batch), 1))))
    predictions = X_batch_with_bias.dot(theta)
    errors = predictions - y_batch
    gradients = (1/effective_batch_size) * X_batch_with_bias.T.dot(errors)
    return gradients

def synchronized_distributed_sgd(X, y, batch_size, learning_rate, num_iterations, num_workers):
    theta = np.zeros(X.shape[1] + 1)
    theta_history = [theta.copy()]
    X_split = np.array_split(X, num_workers)
    y_split = np.array_split(y, num_workers)
    
    with Pool(processes=num_workers) as pool:
        for iter in range(num_iterations):
            worker_data = [(X_split[i], y_split[i], theta, batch_size) for i in range(num_workers)]
            gradients = pool.map(compute_gradient, worker_data)
            avg_gradient = np.mean(gradients, axis=0)
            theta = theta - learning_rate * avg_gradient
            theta_history.append(theta.copy())
    
    return theta, np.array(theta_history)

np.random.seed(0)
X = np.random.rand(1000, 2)
y = 7 * X[:, 0] + 1 * X[:, 1] + 1 * np.random.randn(1000)

batch_size = 128
learning_rate = 0.01
num_iterations = 100
num_workers = 4

theta, theta_history = synchronized_distributed_sgd(X, y, batch_size, learning_rate, num_iterations, num_workers)
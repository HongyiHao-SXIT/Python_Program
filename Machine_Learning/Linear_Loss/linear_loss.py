import numpy as np
def linear_loss(X,y,w,b):
    num_train = X.shape[0]
    num_feature = X.shape[1]
    y_hat = np.dot(X,w) + b
    loss = np.sum((y_hat - y)**2) / num_train
    dw = np.dot(X.T, (y_hat - y)) / num_train
    db = np.sum((y_hat - y)) / num_train
    return y_hat, loss, dw, db

def initialize_params(dims):
    w = np.zeros((dims,1))
    b = 0
    return w, b

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

def liner_train(X,y, learning_rate = 0.01, epochs = 10000):
    loss_his = []
    w, b = initialize_params(X.shape[1])
    
    for i in range(1, epochs):
        y_hat, loss, dw, db = linear_loss(X, y, w, b)
        w += -learning_rate * dw
        b += -learning_rate * db
        loss_his.append(loss)
        
        if i % 10000 == 0:
            print('epoch %d loss %f' %(i, loss))
            
        params = {'w': w, 'b' : b}
        grads = {'dw' : dw, 'db' : db}
        return loss_his, params, grads

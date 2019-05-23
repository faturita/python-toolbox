#coding: latin-1

# Python 3 !

import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split


data = load_breast_cancer()['data']
target = load_breast_cancer()['target']


X_train, X_test, y_train, y_test = train_test_split(data, target, test_size=0.2, shuffle=True)

def sigmoid(x):
    return np.maximum(np.minimum(1 / (1 + np.exp(-x)), 0.9999), 0.0001)

def cost_function(x, y, theta):
    t = x.dot(theta)
    return -(np.sum(y * np.log(sigmoid(t)) + (1-y) * np.log(1-sigmoid(t))) / x.shape[0])


def gradient_cost_function(x, y, theta):
    t = x.dot(theta)
    return x.T.dot(y-sigmoid(t)) / x.shape[0]

def update_theta(x, y, theta, learning_rate):
    return theta + learning_rate * gradient_cost_function(x, y, theta)

def train(x, y, learning_rate, iterations=500, threshold=0.0005):
    theta = np.zeros(x.shape[1])
    costs = []
    print("Start training")
    for i in range(iterations):
        theta = update_theta(x, y, theta, learning_rate)
        cost = cost_function(x, y, theta)
        print(f'[Training step #{i}]-Cost function: {cost:.4f}')
        costs.append({'cost': cost, 'weights': theta})
        if i > 15 and abs(costs[-2]['cost']-costs[-1]['cost']) < threshold:
            break
    return theta, costs

theta, costs = train(X_train, y_train, learning_rate=0.0001)

def predict(x, theta):
    return (sigmoid(x.dot(theta)) >= 0.5).astype(int)


def get_accuracy(x, y, theta):
    y_pred = predict(x, theta)
    return (y_pred == y).sum() / y.shape[0]

print(f'Accuracy on the training set: {get_accuracy(X_train, y_train, theta)}')
print(f'Accuracy on the test set: {get_accuracy(X_test, y_test, theta)}')


plt.figure(figsize=(10,5))
plt.title("Model accuracy depending on the training step")
plt.plot(np.arange(0, len(costs)), [get_accuracy(X_train, y_train, c['weights']) for c in costs],alpha=0.7,label='Train', color='r')
plt.plot(np.arange(0, len(costs)),[get_accuracy(X_test, y_test, c['weights']) for c in costs],alpha=0.7,label='Test', color='b')
plt.xlabel("Number of iterations")
plt.ylabel("Accuracy, %")
plt.legend(loc='best')
plt.grid(True)
plt.xticks(np.arange(0, len(costs)+1, 40))
plt.yticks(np.arange(0.5, 1, 0.1))
plt.show()


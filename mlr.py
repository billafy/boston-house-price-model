import numpy as np

X = np.array([[1, 1], [1, 2], [1, 3]])

y = np.array([2, 4, 6])

(m, n) = X.shape

def hypothesis(theta, x) : 
    return np.dot(x, theta)

lam = 1

def costFunction(theta) : 
    J = (1 / (2 * m)) * sum((hypothesis(theta, X) - y) ** 2)  + (lam * sum(theta[1:] ** 2) )
    return J

theta = np.array([0, 2])

print(costFunction(theta))
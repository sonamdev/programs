import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def forward_propagation(inputs, weights, biases):
    z1 = np.dot(inputs, weights['W1']) + biases['b1']
    a1 = sigmoid(z1)
    z2 = np.dot(a1, weights['W2']) + biases['b2']
    a2 = sigmoid(z2)
    return a2

# Example data
X = np.array([
    [5, 8],
    [2, 4],
    [8, 7],
    [1, 3]
])

y = np.array([[1], [0], [1], [0]])

# Neural network architecture
input_size = 2
hidden_size = 3
output_size = 1

np.random.seed(42)
weights = {
    'W1': np.random.rand(input_size, hidden_size),
    'W2': np.random.rand(hidden_size, output_size)
}

biases = {
    'b1': np.zeros((1, hidden_size)),
    'b2': np.zeros((1, output_size))
}

# Forward propagation
predictions = forward_propagation(X, weights, biases)

# Plotting
plt.scatter(X[:, 0], X[:, 1], c=predictions[:, 0], cmap='viridis', edgecolors='k', marker='o')
plt.title('Neural Network Decision Boundary')
plt.xlabel('Study Hours')
plt.ylabel('Sleep Hours')
plt.colorbar(label='Predicted Probability of Passing')
plt.show()

import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

def forward_propagation(inputs, weights, biases):
    z1 = np.dot(inputs, weights['W1']) + biases['b1']
    a1 = sigmoid(z1)
    z2 = np.dot(a1, weights['W2']) + biases['b2']
    a2 = sigmoid(z2)
    return a1, a2

def backward_propagation(inputs, targets, weights, biases, a1, a2, learning_rate=0.1):
    error_output = targets - a2
    delta_output = error_output * sigmoid_derivative(a2)

    error_hidden = delta_output.dot(weights['W2'].T)
    delta_hidden = error_hidden * sigmoid_derivative(a1)

    weights['W2'] += a1.T.dot(delta_output) * learning_rate
    biases['b2'] += np.sum(delta_output, axis=0, keepdims=True) * learning_rate

    weights['W1'] += inputs.T.dot(delta_hidden) * learning_rate
    biases['b1'] += np.sum(delta_hidden, axis=0, keepdims=True) * learning_rate

def train_neural_network(inputs, targets, weights, biases, epochs=1000, learning_rate=0.1):
    errors = []

    for epoch in range(epochs):
        a1, a2 = forward_propagation(inputs, weights, biases)
        backward_propagation(inputs, targets, weights, biases, a1, a2, learning_rate)

        # Calculate mean squared error for monitoring
        error = np.mean((targets - a2) ** 2)
        errors.append(error)

    return errors

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

# Random weights and biases initialization
np.random.seed(42)
weights = {
    'W1': np.random.rand(input_size, hidden_size),
    'W2': np.random.rand(hidden_size, output_size)
}

biases = {
    'b1': np.zeros((1, hidden_size)),
    'b2': np.zeros((1, output_size))
}

# Training the neural network
errors = train_neural_network(X, y, weights, biases, epochs=10000, learning_rate=0.1)

# Plotting the training error over epochs
plt.plot(errors)
plt.title('Training Error over Epochs')
plt.xlabel('Epochs')
plt.ylabel('Mean Squared Error')
plt.show()

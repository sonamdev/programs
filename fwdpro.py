import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def forward_propagation(X, weights, biases):
    # Input layer to hidden layer
    z1 = np.dot(X, weights['W1']) + biases['b1']
    a1 = sigmoid(z1)

    # Hidden layer to output layer
    z2 = np.dot(a1, weights['W2']) + biases['b2']
    a2 = sigmoid(z2)

    return a2  # Output of the neural network

# Example data
input_size = 3
hidden_size = 4
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

# Input data
X = np.array([[0.5, 0.6, 0.1]])

# Forward propagation
output = forward_propagation(X, weights, biases)

print("Input:", X)
print("Output:", output)

import numpy as np
import matplotlib.pyplot as plt
#step1 design architecture
input_size=2
hidden_size=3
output_size=1
learning_rate=0.1
epochs=1000

#step2 Intialization
np.random.seed(42)
weight_input_hidden=np.random.rand(input_size,hidden_size)
biases_hidden=np.zeros(1,hidden_size)
weight_hidden_output=np.random.rand(hidden_size,output_size)
biases_output=np.zeros(1,output_size)

#step3 activation function
def sigmoid(x):
    return 1/(1+np.exp(-x))

loses=[]
#step4 mean square error
def mse_loss(y_true,y_predicted):
    return np.mean((y_trur-y_predicted)**2)

#step5 Training data
x= np.array([[0,0],[0,1],[1,0],[1,1]])
y= np.array([[0],[1],[1],[0]])

for epoch in range(epochs):
    hidden_input = np.dot(x, weight_input_hidden) + biases_hidden
    hidden_output = sigmoid(hidden_input)
    output_layer_input = np.dot(hidden_output, weights_hidden_output) + biases_output
    predicted_output = sigmoid(output_layer_input)
    













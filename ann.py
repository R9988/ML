import numpy as np

# Input and output data
X = np.array(([2, 9], [1, 5], [3, 6]), dtype=float)  # two inputs [sleep, study]
y = np.array(([92], [86], [89]), dtype=float)  # one output [Expected % in Exams]

# Normalize input data
X = X / np.amax(X, axis=0)  # maximum of X array longitudinally
y = y / 100

# Sigmoid Function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Derivative of Sigmoid Function
def derivatives_sigmoid(x):
    return x * (1 - x)

# Variable initialization
epoch = 5000  # Setting training iterations
lr = 0.1  # Setting learning rate
inputlayer_neurons = 2  # number of features in data set
hiddenlayer_neurons = 3  # number of hidden layers neurons
output_neurons = 1  # number of neurons at output layer

# Weight and bias initialization
wh = np.random.uniform(size=(inputlayer_neurons, hiddenlayer_neurons))  # weight of the link from input node to hidden node
bh = np.random.uniform(size=(1, hiddenlayer_neurons))  # bias of the link from input node to hidden node
wout = np.random.uniform(size=(hiddenlayer_neurons, output_neurons))  # weight of the link from hidden node to output node
bout = np.random.uniform(size=(1, output_neurons))  # bias of the link from hidden node to output node

# Training loop
for i in range(epoch):
    # Forward Propagation
    hinp1 = np.dot(X, wh)
    hinp = hinp1 + bh
    hlayer_act = sigmoid(hinp)
    outinp1 = np.dot(hlayer_act, wout)
    outinp = outinp1 + bout
    output = sigmoid(outinp)

    # Backpropagation
    EO = y - output
    outgrad = derivatives_sigmoid(output)
    d_output = EO * outgrad
    EH = d_output.dot(wout.T)
    hiddengrad = derivatives_sigmoid(hlayer_act)
    d_hiddenlayer = EH * hiddengrad

    # Weight updates
    wout += hlayer_act.T.dot(d_output) * lr
    wh += X.T.dot(d_hiddenlayer) * lr

    # Bias updates
    bout += np.sum(d_output, axis=0, keepdims=True) * lr
    bh += np.sum(d_hiddenlayer, axis=0, keepdims=True) * lr

# Print results
print("Input: \n" + str(X))
print("Actual Output: \n" + str(y))
print("Predicted Output: \n", output)
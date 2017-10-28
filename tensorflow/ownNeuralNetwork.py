from numpy import exp, array, random, dot

NEURON_COUNT = 8
INPUT_COUNT = 3

class NeuronLayer():
    def __init__(self, number_of_neurons, number_of_inputs_per_neuron):
        self.synaptic_weights = 2 * random.random((number_of_inputs_per_neuron, number_of_neurons)) - 1


class NeuralNetwork():
    def __init__(self, layer1, layer2):
        self.layer1 = layer1
        self.layer2 = layer2

    # Normlaise the input between 0 and 1
    def __sigmoid(self, x):
        return 1 / (1 + exp(-x))

    # returns the confidence level
    def __sigmoid_derivative(self, x):
        return x * (1 - x)

    # We train the neural network through a process of trial and error.
    # Adjusting the synaptic weights each time.
    def train(self, training_set_inputs, training_set_outputs, number_of_training_iterations):
        for iteration in range(number_of_training_iterations):
            # Pass the training set through our neural network
            output_from_layer_1, output_from_layer_2 = self.think(training_set_inputs)

            # Calculate the error for layer 2 (The difference between the desired output
            # and the predicted output).
            layer2_error = training_set_outputs - output_from_layer_2
            layer2_delta = layer2_error * self.__sigmoid_derivative(output_from_layer_2)

            # Calculate the error for layer 1 (By looking at the weights in layer 1,
            # we can determine by how much layer 1 contributed to the error in layer 2).
            layer1_error = layer2_delta.dot(self.layer2.synaptic_weights.T)
            layer1_delta = layer1_error * self.__sigmoid_derivative(output_from_layer_1)

            # Calculate how much to adjust the weights by
            layer1_adjustment = training_set_inputs.T.dot(layer1_delta)
            layer2_adjustment = output_from_layer_1.T.dot(layer2_delta)

            # Adjust the weights.
            self.layer1.synaptic_weights += layer1_adjustment
            self.layer2.synaptic_weights += layer2_adjustment

    # The neural network thinks.
    def think(self, inputs):
        output_from_layer1 = self.__sigmoid(dot(inputs, self.layer1.synaptic_weights))
        output_from_layer2 = self.__sigmoid(dot(output_from_layer1, self.layer2.synaptic_weights))
        return output_from_layer1, output_from_layer2

    # The neural network prints its weights
    def print_weights(self):
        print("    Layer 1 (" + str(NEURON_COUNT) + " neurons, each with " + str(INPUT_COUNT) + " inputs): ")
        print(self.layer1.synaptic_weights)
        print("    Layer 2 (1 neuron, with " + str(NEURON_COUNT) + " inputs):")
        print(self.layer2.synaptic_weights)


def normalise_array(input):
    input[0] /= 100
    input[1] /= 100
    input[2] = input[2]
    return input

if __name__ == "__main__":

    NEURON_COUNT = 4
    INPUT_COUNT = 3

    #Seed the random number generator
    random.seed(1)

    # Create layer 1 (4 neurons, each with 3 inputs)
    layer1 = NeuronLayer(NEURON_COUNT, INPUT_COUNT)

    # Create layer 2 (a single neuron with 4 inputs)
    layer2 = NeuronLayer(1, NEURON_COUNT)

    # Combine the layers to create a neural network
    neural_network = NeuralNetwork(layer1, layer2)

    print("Stage 1) Random starting synaptic weights: ")
    neural_network.print_weights()

    # We need to normalise our dataset
    # opponent speed, opponent health, opponent relative angle, opponent distance, own health, clear shot

    # simplified inputs
    # opponent health, own health, clear shot
    training_set_inputs = array([
        normalise_array([50, 50, 1]),
        normalise_array([40, 50, 1]),
        normalise_array([10, 100, 1]),
        normalise_array([100, 40, 1]),
        normalise_array([25, 10, 1]),
        normalise_array([10, 30, 0]),
        normalise_array([10, 100, 0]),
        normalise_array([100, 40, 0]),
        normalise_array([10, 10, 0]),
        normalise_array([5, 100, 0]),
        normalise_array([22, 12, 0]),
        normalise_array([10, 10, 1]),
        normalise_array([5, 100, 1]),
        normalise_array([22, 12, 1]),
        normalise_array([5, 12, 1])
    ])

    training_set_outputs = array([[1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0]]).T


    # Train the neural network using the training set.
    # Do it 60,000 times and make small adjustments each time.
    neural_network.train(training_set_inputs, training_set_outputs, 60000)

    print("Stage 2) New synaptic weights after training: ")
    neural_network.print_weights()

    # Test the neural network with a new situation.
    print("Stage 3) Considering a new situation false ")
    hidden_state, output = neural_network.think(array(normalise_array([40, 100, 0])))
    print(output)

    # Test the neural network with a new situation.
    print("Stage 3) Considering a new situation  false ")
    hidden_state, output = neural_network.think(array(normalise_array([90, 80, 0])))
    print(output)

    # Test the neural network with a new situation.
    print("Stage 3) Considering a new situation  true ")
    hidden_state, output = neural_network.think(array(normalise_array([40, 80, 1])))
    print(output)

    # Test the neural network with a new situation.
    print("Stage 3) Considering a new situation  true ")
    hidden_state, output = neural_network.think(array(normalise_array([50, 50, 1])))
    print(output)

    # Test the neural network with a new situation.
    print("Stage 3) Considering a new situation  false ")
    hidden_state, output = neural_network.think(array(normalise_array([2, 2, 1])))
    print(output)
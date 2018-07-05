#The ReadME

##boolean_neural_network.py

###This repository contains the python implementation Boolean Neural Networks

###["Implementation of Kohut R et.al Boolean Neural Network in Python"](https://pdfs.semanticscholar.org/3836/1c966b4c7c1a4700769c3debf55398ddf471.pdf)

##Description of the Paper

The discussion is centered around a new neuron (Boolean Neuron) that in the neural network architecture can realise various set of Boolean Functions. The learning algorithm is based on sequential learning. 

**What is Sequential Learning?** The neural networks learning algorithms are broadly divided in two categories, the **sequential learning algorithms and the iterative learning algorithms**. In the former, we have the training dataset beforehand and one construct the neural network by adding neurons, layers , the training algorithms takes a lesser training time and assures fast convergence. In the latter, we first fix the network architecture and then using iteration change the trainable parameters i.e the weights, bias, etc using certain optimisers and error gradients. The examples **Functional on Tabular Function Set (FTFS) and Expand and Truncate Learning (ETL)** falls under Sequential Learning, whereas the **Back Propagation Algorithms and Radical Basis Function (RBF)** falls under the  Iterative Learning category.

The neural network model supports only a single hidden layer, requires entire truth table for training, and works fine with **multi-output functions**. The model fails to utilise the integral functionality of the neural network and ends up in more of an representation model similar to BDDs, AIGs etc. However, it helps to realise the important **intermediate logic** function in the representation.

##How to run?
```bash
>git clone <url>
>cd boolean_neural_network
>python main.py <truth table file with outputs in order seperated by,> <no of input> <no of outputs>


```
##Conclusion 

However, this is a very quick implementation and can be modified easilty accoeding to the use.

Thanks

Code
====
To use ArrayLSTM into your own project, you can use it as a standalone module.
Here we show some simple examples on how to use the ArrayLSTM package in your own python code.
For a complete documentation we refer to the :ref:`Reference` guide.

Import
^^^^^^
To import components from ArrayLSTM simply use the following format

.. code:: python

  from arrayLSTM import <Object>
  from arrayLSTM.extensions import <Object>

For example, the following code imports the different LSTM objects as found in the :ref:`Reference`.

.. code:: python

  # Imports
  from arrayLSTM            import LSTM
  from arrayLSTM            import ArrayLSTM
  from arrayLSTM.extensions import AttentionArrayLSTM
  from arrayLSTM.extensions import StochasticArrayLSTM

Working example
^^^^^^^^^^^^^^^

In this example, we import all different LSTM implementations and use it to predict the next item in a sequence.
First we import the necessary torch modules and different LSTMs that we want to use.

.. code:: python

  # Torch imports
  import torch
  import torch.nn as nn
  import torch.nn.functional as F

  # ArrayLSTM imports
  from arrayLSTM            import LSTM
  from arrayLSTM            import ArrayLSTM
  from arrayLSTM.extensions import AttentionArrayLSTM
  from arrayLSTM.extensions import StochasticArrayLSTM

Second, we generate some random data

.. code:: python

  # Parameters to use
  n_samples   = 1024
  seq_length  = 10
  size_input  = 10
  size_hidden = 128
  size_output = 10
  k           = 4

  # Generate random input data
  X = (size_input*torch.rand((n_samples, seq_length))).to(torch.int64)

Next, we create a Neural Network with our LSTM of choice.
Please note that this is a very simple example in which we show how the StochasticArrayLSTM can be used as a simple module.

.. code:: python

  class MyNetwork(nn.Module):

    def __init__(self, size_input, size_hidden, size_output, k):
      # Call super method
      super().__init__()

      # Set variables
      self.size_input  = size_input
      self.size_hidden = size_hidden
      self.size_output = size_output
      self.k           = k

      # Initialise layers
      self.lstm    = StochasticArrayLSTM(size_input, size_hidden, k) # Use any LSTM of your choosing
      self.linear  = nn.Linear(size_hidden, size_output)
      self.softmax = nn.LogSoftmax(dim=1)

    def forward(self, X):
      # One-hot encode input - transforms input into one-hot-encoded input
      encoded = F.one_hot(X, self.size_input).to(torch.float32)

      # Pass through LSTM layer
      out, (hidden, state) = self.lstm(encoded)
      # Take hidden state as output
      hidden = hidden.squeeze(0)

      # Pass through linear layer
      out = self.linear(hidden)
      # Perform softmax and return
      return self.softmax(out)

Finally, we can call the network using the data and perform further training, which we leave up to the user.

.. code:: python

  # Create an instance of MyNetwork
  net = MyNetwork(size_input, size_hidden, size_output, k)
  # Pass the input data X through the network
  output = net(X)

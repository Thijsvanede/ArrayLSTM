.. _StochasticArrayLSTM:

StochasticArrayLSTM
===================
The StochasticArrayLSTM implements an ArrayLSTM with Non-deterministic Array-LSTM extension "Stochastic Output Pooling" of Rocki's Recurrent Memory Array Structures.
It module is build as an extension of the basic :ref:`ArrayLSTM` implementation.

.. _`torch.nn.Module`: https://pytorch.org/docs/stable/nn.html#module

.. autoclass:: extensions.StochasticArrayLSTM

Initialization
^^^^^^^^^^^^^^

.. automethod:: extensions.StochasticArrayLSTM.__init__

Forward
^^^^^^^

The StochasticArrayLSTM overwrites ArrayLSTM's :py:meth:`update_hidden()` method to update the hidden state using stochastic output pooling.
The API is equivalent to that of :ref:`ArrayLSTM`, but the implementations differ.

.. automethod:: extensions.StochasticArrayLSTM.update_hidden

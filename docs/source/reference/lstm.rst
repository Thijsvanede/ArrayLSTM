.. _LSTM:

LSTM
====
As a basis, we provide a pure pytorch implementation of the LSTM module.
This extends the regular `torch.nn.Module`_ interface.

.. _`torch.nn.Module`: https://pytorch.org/docs/stable/nn.html#module

.. autoclass:: lstm.LSTM

Initialization
^^^^^^^^^^^^^^

.. automethod:: lstm.LSTM.__init__

Forward
^^^^^^^

As all nn.Module objects, the LSTM implements a :py:meth:`forward()` method.
This method forwards all sequences in x through the :py:meth:`forward_cell()` method.

.. automethod:: lstm.LSTM.forward

A single LSTM cell is implemented by the :py:meth:`forward_cell()` method.
Note that this method is also overwritten by subclasses to implement their custom forward methods.

.. automethod:: lstm.LSTM.forward_cell


Hidden state
^^^^^^^^^^^^

The LSTM provides a method for initializing the hidden state and cell state.
Note that this method is also overwritten by subclasses to implement their custom cell initializations.

.. automethod:: lstm.LSTM.initHidden

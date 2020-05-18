.. _ArrayLSTM:

ArrayLSTM
=========
The ArrayLSTM implements the basic ArrayLSTM of Rocki's Recurrent Memory Array Structures.
It module is build as an extension of the normal :ref:`LSTM` implementation.

.. _`torch.nn.Module`: https://pytorch.org/docs/stable/nn.html#module

.. autoclass:: arraylstm.ArrayLSTM

Initialization
^^^^^^^^^^^^^^

.. automethod:: arraylstm.ArrayLSTM.__init__

Forward
^^^^^^^

A single ArrayLSTM cell is implemented by the :py:meth:`forward_cell()` method.
This method overwrites its :ref:`LSTM` superclass.

.. automethod:: arraylstm.ArrayLSTM.forward_cell

As variations of the ArrayLSTM update their hidden state differently, we also add a method :py:meth:`forward_cell()`.
This method can be overwritten by subclasses to update the hidden state in different ways.

.. automethod:: arraylstm.ArrayLSTM.update_hidden


Hidden state
^^^^^^^^^^^^

The ArrayLSTM requires multiple cell states instead of a single one, therefore it overwrites it super method from :ref:`LSTM`.

.. automethod:: arraylstm.ArrayLSTM.initHidden

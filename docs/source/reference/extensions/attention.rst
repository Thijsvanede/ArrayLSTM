.. _AttentionArrayLSTM:

AttentionArrayLSTM
==================
The AttentionArrayLSTM implements an ArrayLSTM with Deterministic Array-LSTM extension "Lane selection: Soft Attention" of Rocki's Recurrent Memory Array Structures.
It module is build as an extension of the basic :ref:`ArrayLSTM` implementation.

.. _`torch.nn.Module`: https://pytorch.org/docs/stable/nn.html#module

.. autoclass:: extensions.AttentionArrayLSTM

Initialization
^^^^^^^^^^^^^^

.. automethod:: extensions.AttentionArrayLSTM.__init__

Forward
^^^^^^^

The AttentionArrayLSTM overwrites ArrayLSTM's :py:meth:`forward_cell()` method to include an attention mechanism.
The API is equivalent to that of :ref:`ArrayLSTM`, but the implementations differ.

.. automethod:: extensions.AttentionArrayLSTM.forward_cell

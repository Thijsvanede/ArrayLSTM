Installation
============
The most straigtforward way of installing ArrayLSTM is via pip

.. code::

  pip install array-lstm

From source
^^^^^^^^^^^

If you wish to stay up to date with the latest development version, you can instead download the `source code`_.
In this case, make sure that you have all the required `dependencies`_ installed.

Once the dependencies have been installed, run:

.. code::

  pip install -e <path/to/directory/containing/arraylstm/setup.py>

.. _source code: https://github.com/Thijsvanede/ArrayLSTM

.. _dependencies:

Dependencies
^^^^^^^^^^^^
ArrayLSTM requires the following python packages to be installed:

- pytorch: https://pytorch.org/

All dependencies should be automatically downloaded if you install ArrayLSTM via pip. However, should you want to install these libraries manually, you can install the dependencies using the requirements.txt file

.. code::

  pip install -r requirements.txt

Or you can install these libraries yourself

.. code::

  pip install -U torch

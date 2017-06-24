Learning Python
===============
Follow the book Learning Pyghon to learn Python.  Most codes are in :code:`tests/`.

Load Python
-----------
Initialize Python environment

.. code-block:: bash

    module add conda
    source activate py3

Initialize Sphinx
-----------------
In the root directory of a Python project,

.. code-block:: bash

    sphinx-quickstart

.. code-block:: text

    Enter the root path for documentation.
    > Root path for the documentation [.]: docs
    > Separate source and build directories (y/n) [n]:
    > Name prefix for templates and static dir [_]:
    > Project name: Learning Python
    > Author name(s): Yi-Kun Yang
    > Project version []: 0.0.1
    > Project release [0.0.1]:
    > Project language [en]:
    > Source file suffix [.rst]:
    > Name of your master document (without suffix) [index]:
    > Do you want to use the epub builder (y/n) [n]: y
    > autodoc: automatically insert docstrings from modules (y/n) [n]: y
    ... yes to all the extensions ...  There are ones that conflict but it is all right.
    > Create Makefile? (y/n) [y]:
    > Create Windows command file? (y/n) [y]:

Add an :code:`html` task to the :code:`Makefile` in the project root directory

.. code-block:: makefile

    html:
	    sphinx-apidoc -o docs . tests setup.py
	    make -C docs html

Modify :code:`conf.py` to enable

.. code-block:: python

    import os
    import sys
    sys.path.insert(0, os.path.abspath('..'))

In the next step, we link :code:`README.rst` to Sphinx documentation.
Create :code:`docs/readme.rst` with the following content

.. code-block:: rst

    .. include:: ../README.rst

Modify :code:`docs/index.rst`

.. code-block:: rst

    .. toctree:: rst
        :maxdepth: 2
        :caption: Contents:

        readme  # Not necessary
        modules  # Not necessary, just to shut the warning up

Test
----
.. code-block:: bash

    python -m unittet

or simply

.. code-block:: sh

    make test

